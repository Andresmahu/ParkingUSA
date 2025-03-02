import React from "react";
import { createStackNavigator } from "@react-navigation/stack";
import { NavigationContainer } from "@react-navigation/native";

// Asegúrate de que las rutas sean correctas
import LoginS from "../screens/LoginS";
import RegisterS from "../screens/RegisterS";

const Stack = createStackNavigator();

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen
          name="Login"
          component={LoginS}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="Register"
          component={RegisterS}
          options={{ headerShown: false }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
