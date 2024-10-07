import React from 'react'
import css from "./styles.module.css"

const Form = () => {
  return (
    <section className={css.form__section}>
        <div className="container">
            <div className={css.form__inner}>
                <form className={css.form}>
                    <label>
                        <input type="file" />
                        <input type="text" />
                    </label>
                    <button type='submit'>Submit</button>
                </form>
            </div>
        </div>
    </section>
  )
}

export default Form
