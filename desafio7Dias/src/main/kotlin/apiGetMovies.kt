import com.google.gson.GsonBuilder
import com.squareup.moshi.Moshi
import com.squareup.moshi.Types
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Header
import utils.NetWork

interface EndPointFilme {

    @GET(" ")
    fun getMovies(
        @Header("X-RapidAPI-Key") apiKey: String,
        @Header("X-RapidAPI-Host") apiHost: String
    ): Call<ResponseBody>

}


class ApiOmdb {

    fun loadApiAndConnect(): Pair<List<FilmeOmdbScrap>?, String> {
        val retrofitClient = NetWork.getRetrofitInstance("https://imdb-top-100-movies1.p.rapidapi.com/")
        val endPoint = retrofitClient.create(EndPointFilme::class.java)

        val response = endPoint.getMovies(
            "@df92179ac7mshf88cfb2684116a6p122b3ajsn70828838e76c",
            "imdb-top-100-movies1.p.rapidapi.com"
        ).execute()

        //retorna ultimo valor declarado de forma explicita.
        return if (response.isSuccessful) {
            val response = response.body()

            val moshi = Moshi.Builder().build()
            val type = Types.newParameterizedType(List::class.java, FilmeOmdbScrap::class.java)

            val moshiResponde = moshi.adapter<List<FilmeOmdbScrap>>(type).fromJson(response?.string()) ?: emptyList()

            val gson = GsonBuilder().setPrettyPrinting().create()
            val jsonFormatado = gson.toJson(moshiResponde)

            Pair(moshiResponde,jsonFormatado)

        } else {
            Pair(null, "")
        }

    }

//Tentativa de fazer a chamada da funcao assíncrona.
//    fun loadApiAndConnect(): List<FilmeOmdbScrap> {
//        val retrofitClient = NetWork.getRetrofitInstance("https://imdb-top-100-movies1.p.rapidapi.com/")
//        val endPoint = retrofitClient.create(EndPointFilme::class.java)
////        var filmes: List<FilmeOmdbScrap> = emptyList()
//
//        endPoint.getMovies(
//            "df92179ac7mshf88cfb2684116a6p122b3ajsn70828838e76c",
//            "imdb-top-100-movies1.p.rapidapi.com"
//        ).enqueue(object : Callback<ResponseBody> {
//            override fun onResponse(
//                call: Call<ResponseBody>,
//                response: Response<ResponseBody>
//            ) {
//
////                if (response.isSuccessful) {
////                    //save txt format
////                    val response = response.body()
////
////                    val moshi = Moshi.Builder().build()
////
////                    val type = Types.newParameterizedType(List::class.java, FilmeOmdbScrap::class.java)
////                    var filmes = moshi.adapter<List<FilmeOmdbScrap>>(type).fromJson(response?.string()) ?: emptyList()
////
////                }
//            }
//
//            override fun onFailure(call: Call<ResponseBody>, t: Throwable) {
//                TODO("Not yet implemented")
//            }
//        })
//
//    }

}