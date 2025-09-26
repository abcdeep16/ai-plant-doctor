import React from "react";

const Footer = () => {
  return (
    <footer className="bg-green-800 text-white py-6 mt-10">
      <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center">
        <p>© {new Date().getFullYear()} KrishiBot. All rights reserved.</p>
        <div className="space-x-6 mt-4 md:mt-0">
          <a href="#privacy" className="hover:text-yellow-300">Privacy</a>
          <a href="#terms" className="hover:text-yellow-300">Terms</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
