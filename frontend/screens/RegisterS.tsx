import React from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
} from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { LinearGradient } from "expo-linear-gradient";

export default function RegisterScreen({ navigation }) {
  return (
    <LinearGradient colors={["#1a0025", "#45005a"]} style={styles.container}>
      <TouchableOpacity
        onPress={() => navigation.goBack()}
        style={styles.backButton}
      >
        <Ionicons name="arrow-back" size={24} color="#fff" />
      </TouchableOpacity>

      <Text style={styles.title}>Registro</Text>

      <TextInput
        style={styles.input}
        placeholder="Tu Nombre"
        placeholderTextColor="#999"
      />
      <TextInput
        style={styles.input}
        placeholder="Tus Apellidos"
        placeholderTextColor="#999"
      />
      <TextInput
        style={styles.input}
        placeholder="example@email.com"
        placeholderTextColor="#999"
      />
      <TextInput
        style={styles.input}
        placeholder="Introduce tu contraseña"
        placeholderTextColor="#999"
        secureTextEntry
      />

      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>REGISTRARME</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={() => navigation.navigate("Login")}>
        <Text style={styles.loginText}>¿Ya tienes cuenta? Inicia Sesión</Text>
      </TouchableOpacity>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    paddingHorizontal: 20,
  },
  backButton: { position: "absolute", top: 40, left: 20 },
  title: { fontSize: 28, color: "#fff", fontWeight: "bold", marginBottom: 20 },
  input: {
    width: "100%",
    height: 50,
    backgroundColor: "rgba(255,255,255,0.1)",
    borderRadius: 10,
    paddingLeft: 15,
    marginBottom: 15,
    color: "#fff",
  },
  button: {
    width: "100%",
    height: 50,
    backgroundColor: "#ff00ff",
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 10,
  },
  buttonText: { color: "#fff", fontWeight: "bold", fontSize: 16 },
  loginText: { color: "#fff", marginTop: 15, fontWeight: "bold" },
});
