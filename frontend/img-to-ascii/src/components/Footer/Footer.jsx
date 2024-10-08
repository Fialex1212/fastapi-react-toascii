import css from "./styles.module.css";
import { FaGithub } from "react-icons/fa";

const Footer = () => {
  return (
    <footer className={css.footer}>
      <div className="container">
        <div className={css.footer__inner}>
          <p className={css.footer__text}>
            IMG to ASCI © 2024, All Rights Reserved
          </p>
          <a className={css.footer__link} href="https://github.com/Fialex1212/">
            <FaGithub className={css.footer__github} width={24} hanging={24} />
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
