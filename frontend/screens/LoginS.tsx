import React from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Image,
  StyleSheet,
} from "react-native";
import { LinearGradient } from "expo-linear-gradient";

export default function LoginScreen({ navigation }) {
  return (
    <LinearGradient colors={["#1a0025", "#45005a"]} style={styles.container}>
      <Image source={require("../assets/login-logo.png")} style={styles.logo} />
      <Text style={styles.title}>Bienvenido</Text>
      <Text style={styles.subtitle}>Inicia sesión en ParkSide</Text>

      <TextInput
        style={styles.input}
        placeholder="Correo"
        placeholderTextColor="#999"
      />
      <TextInput
        style={styles.input}
        placeholder="Contraseña"
        placeholderTextColor="#999"
        secureTextEntry
      />

      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>INICIAR SESIÓN</Text>
      </TouchableOpacity>

      <TouchableOpacity>
        <Text style={styles.forgotPassword}>He olvidado mi contraseña</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={() => navigation.navigate("Register")}>
        <Text style={styles.registerText}>¿No tienes cuenta? Regístrate</Text>
      </TouchableOpacity>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: "center", alignItems: "center" },
  logo: { width: 150, height: 150, marginBottom: 20 },
  title: { fontSize: 28, color: "#fff", fontWeight: "bold" },
  subtitle: { fontSize: 16, color: "#ddd", marginBottom: 20 },
  input: {
    width: "80%",
    height: 50,
    backgroundColor: "rgba(255,255,255,0.1)",
    borderRadius: 10,
    paddingLeft: 15,
    marginBottom: 15,
    color: "#fff",
  },
  button: {
    width: "80%",
    height: 50,
    backgroundColor: "#ff00ff",
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 10,
  },
  buttonText: { color: "#fff", fontWeight: "bold", fontSize: 16 },
  forgotPassword: { color: "#ddd", marginTop: 10 },
  registerText: { color: "#fff", marginTop: 15, fontWeight: "bold" },
});
