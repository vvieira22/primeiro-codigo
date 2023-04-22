// Copyright 2000-2021 JetBrains s.r.o. and contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.
@file:OptIn(ExperimentalComposeUiApi::class)

import androidx.compose.desktop.ui.tooling.preview.Preview
import androidx.compose.foundation.ExperimentalFoundationApi
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.lazy.items
import androidx.compose.material.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.produceState
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.painter.BitmapPainter
import androidx.compose.ui.graphics.painter.Painter
import androidx.compose.ui.graphics.toComposeImageBitmap
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.DpSize
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.WindowPosition
import androidx.compose.ui.window.application
import androidx.compose.ui.window.rememberWindowState
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.jetbrains.skia.Image
import utils.OperacoesArquivo
import java.io.BufferedInputStream
import java.io.ByteArrayOutputStream
import java.io.IOException
import java.net.URL
import javax.imageio.ImageIO

var defaultWidth = Modifier.width(140.dp)
var defaultFontSize = 15.sp

@OptIn(ExperimentalFoundationApi::class)
@Composable
@Preview
fun App() {
    MaterialTheme {
        Surface(
            color = Color.Black
        ) {
            Box(
                modifier = Modifier.fillMaxSize()
            ) {
                val listaFilmes = tratarListaFilmes()
                LazyVerticalGrid(columns = GridCells.Adaptive(150.dp)) {
                        items(listaFilmes)
                        { filme ->
                            inserirFilmeNaTela(filme)
                        }
                }
            }
        }
    }
}

@OptIn(ExperimentalMaterialApi::class)
fun aplicacao() = application {
    val windowState = rememberWindowState(
        size = DpSize(width = 800.dp, height = 600.dp),
        position = WindowPosition(Alignment.Center)
    )

    Window(
        onCloseRequest = ::exitApplication,
        state = windowState,
        title = "Lista Filmes e Séries IMDB"
    ) {
        App()
    }
}

fun main() {
    tratarListaFilmes()
    aplicacao()
}

//conecta a api e atualiza o .txt contendo os filmes.
fun tratarListaFilmes(): List<FilmeOmdbScrap> {

    val retornoApi = ApiOmdb().loadApiAndConnect()

    try {
        if (retornoApi != Pair(null, "")) {
            if (retornoApi.first != null) {
                OperacoesArquivo.saveJsonTxt("src/main/resources/imdb-100.txt", retornoApi.second)
                return retornoApi.first!!.mapNotNull { it }
            }
        }
        //tentando puxar backup anterior offline
        else {
            return OperacoesArquivo.loadJsonToFilme("src/main/resources/imdb-100.txt").mapNotNull { it }
        }
    } catch (e: Throwable) {
    }
    throw IllegalStateException("erro ao carregar informações da base de dados imdb")
}

@Composable
fun inserirFilmeNaTela(filme: FilmeOmdbScrap) {

    var url = filme.image[0][1]
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        AsyncImage(
            load = { url.loadImageBitmap() },
            painterFor = { remember { BitmapPainter(it) } },
            contentDescription = "Sample",
            modifier = Modifier.width(140.dp)
        )
//        Image(
//            url.loadImageBitmap(),
//            contentDescription = null,
//            modifier = defaultWidth,
//            contentScale = ContentScale.Crop,
//        )
        Row(
            modifier = defaultWidth,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Row()
            {
                Icon(
                    painterResource("star.png"),
                    contentDescription = null, modifier = Modifier.width(13.dp),
                    tint = Color.Yellow
                )
                Text(
                    "${filme.rating}",
                    color = Color.White,
                    modifier = Modifier
                        .align(Alignment.CenterVertically)
                        .padding(start = 3.dp),
                    fontSize = defaultFontSize
                )
            }
//            Text(
//                "1999-todo",
//                color = Color.White,
//                modifier = Modifier.align(Alignment.CenterVertically),
//                fontSize = defaultFontSize
//            )
        }
        Row(
            modifier = defaultWidth,
            horizontalArrangement = Arrangement.Center
        ) {
            Text(
                filme.title,
                color = Color.White,
                style = TextStyle(textAlign = TextAlign.Center),
                softWrap = true,
                modifier = Modifier.align(Alignment.CenterVertically),
                fontSize = defaultFontSize
            )
        }
    }
}

fun cadastrarFilmes(): List<Filme> {

    return listOf(
        Filme(
            titulo = "Neon Genesis Evangelion",
            dataLancamento = "1995",
            nota = 8.5,
            urlCapa = "https://m.media-amazon.com/images/M/MV5BZWNhNmViYTQtZGIxZS00ZjlkLWE5NDctZmQ5MzE5MDFkNTgyXkEyXkFqcGdeQXVyMjQ5MjYwNDE@._V1_FMjpg_UY714_.jpg"
        ),
        Filme(
            titulo = "O Poderoso Chefão",
            dataLancamento = "1972",
            nota = 9.2,
            urlCapa = "https://m.media-amazon.com/images/M/MV5BZjgwNzE5ODgtYzAyZC00YTZhLThhNDktMDVlOGNhYzk5NTVkXkEyXkFqcGdeQXVyMTAzMDM4MjM0._V1_.jpg"
        ),
        Filme(
            titulo = "Batman: O Cavaleiro das Trevas",
            dataLancamento = "2008",
            nota = 9.0,
            urlCapa = "https://m.media-amazon.com/images/M/MV5BM2E1ZjEyYWQtMjgyMy00ZTkwLThkM2QtN2YwM2NmYzAyYjE0XkEyXkFqcGdeQXVyMTAzMDM4MjM0._V1_.jpg"
        ),
        Filme(
            titulo = "Matrix",
            dataLancamento = "1999",
            nota = 8.7,
            urlCapa = "https://m.media-amazon.com/images/M/MV5BOTgyZTcyOGEtZmVhMC00Mzc2LTgyYWItZWFhM2RmNTRlZTM0XkEyXkFqcGdeQXVyNDQ0MTYzMDA@._V1_.jpg"
        )
    )
}

fun String.loadImageBitmap(): ImageBitmap {
    val inputStream = BufferedInputStream(
        URL(this).openStream()
    )
    val bufferedImage = ImageIO.read(inputStream)

    val stream = ByteArrayOutputStream()
    ImageIO.write(bufferedImage, "jpg", stream)
    val byteArray = stream.toByteArray()

    return Image.makeFromEncoded(byteArray).toComposeImageBitmap()
}


//https://github.com/JetBrains/compose-multiplatform/tree/master/tutorials/Image_And_Icons_Manipulations
@Composable
fun <T> AsyncImage(
    load: suspend () -> T,
    painterFor: @Composable (T) -> Painter,
    contentDescription: String,
    modifier: Modifier = Modifier,
    contentScale: ContentScale = ContentScale.Fit,
) {
    val image: T? by produceState<T?>(null) {
        value = withContext(Dispatchers.IO) {
            try {
                load()
            } catch (e: IOException) {
                // instead of printing to console, you can also write this to log,
                // or show some error placeholder
                e.printStackTrace()
                null
            }
        }
    }

    if (image != null) {
        Image(
            painter = painterFor(image!!),
            contentDescription = contentDescription,
            contentScale = contentScale,
            modifier = modifier
        )
    }
}