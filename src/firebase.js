// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyCP0BVKpFC2ikrKWCcBCF1GEhnloWLbE7M",
  authDomain: "lista-nombres-24735.firebaseapp.com",
  projectId: "lista-nombres-24735",
  storageBucket: "lista-nombres-24735.firebasestorage.app",
  messagingSenderId: "486119917025",
  appId: "1:486119917025:web:4736260d3a165b5e377ea0",
  measurementId: "G-RMRR6X0JWQ"
};

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);