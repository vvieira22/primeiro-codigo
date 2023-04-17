// Copyright 2000-2021 JetBrains s.r.o. and contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.
@file:OptIn(ExperimentalComposeUiApi::class)

import androidx.compose.material.MaterialTheme
import androidx.compose.desktop.ui.tooling.preview.Preview
import androidx.compose.foundation.layout.Column
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.width
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import org.jetbrains.skia.Image
import java.io.BufferedInputStream
import java.io.ByteArrayOutputStream
import java.net.URL
import javax.imageio.ImageIO
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.toComposeImageBitmap
import androidx.compose.ui.unit.DpSize
import androidx.compose.ui.window.WindowPosition
import androidx.compose.ui.window.rememberWindowState

@Composable
@Preview
fun App() {
    MaterialTheme {
        chamarFilme().let{ filme ->
            Column {
                Text(filme.titulo)

                //can you use Coil package to do this more easy
                Image(filme.urlCapa
                    .loadImageBitmap(),
                    contentDescription = null,
                    modifier=Modifier.width(200.dp))

                Text("Nota: ${filme.nota} - Ano: ${filme.dataLancamento} ")

                /*
                offline load image

                Image(painterResource("evangelion.png"),
                    contentDescription = null, modifier=Modifier.width(200.dp))

                */
            }
        }
    }
}

fun main() = application {
    val windowState = rememberWindowState(
        size = DpSize(width = 800.dp, height = 600.dp),
        position = WindowPosition(Alignment.Center),
    )

    Window(onCloseRequest = ::exitApplication, state = windowState
    ) {

        App()
    }
}

@Composable
fun chamarFilme(): Filme{
    var filme = Filme(
        titulo = "Neon Genesis Evangelion",
        dataLancamento = "1995 - 1996",
        nota = 8.5,
        urlCapa = "https://m.media-amazon.com/images/M/MV5BZWNhNmViYTQtZGIxZS00ZjlkLWE5NDctZmQ5MzE5MDFkNTgyXkEyXkFqcGdeQXVyMjQ5MjYwNDE@._V1_FMjpg_UY714_.jpg"
    )
    return filme
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
