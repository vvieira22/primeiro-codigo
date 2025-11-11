import 'package:firebase_auth/firebase_auth.dart' hide User;
import '../../models/User.dart';

class AuthFirebase {
  final FirebaseAuth _FireBaseauth = FirebaseAuth.instance;

  Future<String?> entrarUsuario({required String email, required String senha}) async {
    try {
      await _FireBaseauth.signInWithEmailAndPassword(email: email, password: senha);
    } on FirebaseAuthException catch (e) {
      switch(e.code){
        case 'user-not-found':
          return 'Usuário não encontrado';
        case 'wrong-password':
          return 'Senha incorreta';
      }
      return e.code;
    }
    return null;
  }

  Future<String?> cadastrarUsuario(User newUser) async {
    try {
     UserCredential userCredential =  await _FireBaseauth.createUserWithEmailAndPassword(
         email: newUser.email, password: newUser.password);
     await userCredential.user!.updateDisplayName(newUser.name);
    }on FirebaseAuthException catch (e) {
      switch(e.code){
        case 'weak-password':
          return 'Senha fraca';
        case 'email-already-in-use':
          return 'Email já cadastrado, por favor fazer Login';
      }
      return e.code;
    }
    return null;
  }

  Future<String?> redefinirSenha({required String email}) async {
    try {
      await _FireBaseauth.sendPasswordResetEmail(email: email);
    } on FirebaseAuthException catch (e) {
      switch(e.code){
        case 'user-not-found':
          return 'Usuário não encontrado';
      }
      return e.code;
    }
    return null;
  }

  Future<String?> deslogarUsuario() async {
    try {
      await _FireBaseauth.signOut();
    } on FirebaseAuthException catch (e) {
      return e.code;
    }
    return null;
  }

  Future<String?> excluirUsuario({required String senha}) async{
    try {
      await _FireBaseauth.signInWithEmailAndPassword(email: _FireBaseauth.currentUser!.email!, password: senha);
      await _FireBaseauth.currentUser!.delete();
    } on FirebaseAuthException catch (e) {
      return e.code;
    }
    return null;
  }
}