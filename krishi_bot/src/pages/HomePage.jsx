import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";

const HomePage = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />

      {/* Main content */}
      <main className="flex-1 flex items-center justify-center bg-green-50 text-center px-6">
        <h2 className="text-3xl md:text-5xl font-bold text-green-800">
          Welcome to KrishiBot 🌱
        </h2>
      </main>

      <Footer />
    </div>
  );
};

export default HomePage;
