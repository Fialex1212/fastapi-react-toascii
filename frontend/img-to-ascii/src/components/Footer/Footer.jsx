import { FaGithub } from "react-icons/fa";

const Footer = () => {
  return (
    <footer className="bg-[var(--blocks-color)] h-[44px]">
      <div className="container mx-auto h-full px-4 flex justify-between items-center">
        <p className="text-[var(--text-color)] text-sm">
          IMG to ASCI © 2024, All Rights Reserved
        </p>
        <a
          className="w-6 h-6 text-[var(--text-color)] hover:text-blue-200 transition duration-300"
          href="https://github.com/Fialex1212/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <FaGithub className="w-6 h-6" />
        </a>
      </div>
    </footer>
  );
};


export default Footer;
