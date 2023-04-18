// Copyright 2000-2021 JetBrains s.r.o. and contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.
@file:OptIn(ExperimentalComposeUiApi::class)

import androidx.compose.desktop.ui.tooling.preview.Preview
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.Icon
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Surface
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.toComposeImageBitmap
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
import org.jetbrains.skia.Image
import java.io.BufferedInputStream
import java.io.ByteArrayOutputStream
import java.net.URL
import javax.imageio.ImageIO

var defaultWidth = Modifier.width(140.dp)
var defaultFontSize = 15.sp

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
                    val listaFilmes = cadastrarFilmes()
                    LazyColumn {
                        items(listaFilmes) { filme ->
                            inserirFilmeNaTela(filme)
                        }
                    }
                }
            }
        }
    }

fun main() = application {
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

@Composable
fun inserirFilmeNaTela(filme: Filme) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {

        //can you use Coil package to do this more easy
        Image(
            filme.urlCapa
                .loadImageBitmap(),
            contentDescription = null,
            modifier = defaultWidth
        )
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
                    "${filme.nota}",
                    color = Color.White,
                    modifier = Modifier
                        .align(Alignment.CenterVertically)
                        .padding(start = 3.dp),
                    fontSize = defaultFontSize
                )
            }
            Text(
                "${filme.dataLancamento}",
                color = Color.White,
                modifier = Modifier.align(Alignment.CenterVertically),
                fontSize = defaultFontSize
            )
        }
        Row(
            modifier = defaultWidth,
            horizontalArrangement = Arrangement.Center
        ) {
            Text(
                filme.titulo,
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
