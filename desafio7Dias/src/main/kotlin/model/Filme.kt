import com.google.gson.annotations.SerializedName
import com.squareup.moshi.JsonClass

data class Filme(
    val titulo: String,
    val dataLancamento: String,
    val nota: Double,
    val urlCapa: String
)

data class FilmeOmdbScrap(
    val rank: String,
    val rating: String,
    val title: String,
    val image: List<List<String>>
)

