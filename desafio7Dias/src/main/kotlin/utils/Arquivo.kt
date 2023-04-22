package utils

import FilmeOmdbScrap
import com.squareup.moshi.Moshi
import com.squareup.moshi.Types
import java.io.File
import java.io.FileWriter

class Arquivo {
    fun readFile(filePath: String): String {
        val file = File(filePath)
        return file.readText()
    }

    fun writeFile(filePath: String, content: String): Boolean {
        return try {
            val file = File(filePath)
            val writer = FileWriter(file)

            writer.write(content)

            writer.close()
            true
        } catch (e: Throwable) {
            false
        }
    }

    fun fileExists(filePath: String): Boolean {
        val file = File(filePath)
        return file.exists()
    }
}

class OperacoesArquivo {
    companion object {
        var arquivo = Arquivo();
        private fun txtExist(path: String) = arquivo.fileExists(path)

        //fun to
        fun saveJsonTxt(path: String, json: String): Boolean {
            return arquivo.writeFile(path, json);
        }

        fun loadJsonToFilme(filePath: String): List<FilmeOmdbScrap> {
            var jsonStr = arquivo.readFile(filePath)

            val moshi = Moshi.Builder().build()
            val type = Types.newParameterizedType(List::class.java, FilmeOmdbScrap::class.java)
            return  moshi.adapter<List<FilmeOmdbScrap>>(type).fromJson(jsonStr) ?: emptyList()
        }
    }
}
