import React from 'react'
import css from "./styles.module.css"

const Footer = () => {
  return (
    <footer className={css.footer}>
        <div className="container">
            <div className={css.footer__inner}>
                <p className={css.footer__text}>IMG to ASCI © 2024, All Rights Reserved</p>
                <a href="https://github.com/Fialex1212/">github</a>
            </div>
        </div>
    </footer>
  )
}

export default Footer
