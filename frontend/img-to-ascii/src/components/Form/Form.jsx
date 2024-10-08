import React, { useState } from "react";
import css from "./styles.module.css";
import cn from "classnames";
import toast, { Toaster } from "react-hot-toast";
import { PORT } from "../../utils/constans";
import axios from "axios";

const Form = () => {
  const [imgLink, setImgLink] = useState("");
  const [img, setImg] = useState(null);

  const onChangeImg = (e) => {
    e.preventDefault();
    const selectedField = e.target.files[0];
    if (selectedField) {
      setImg(selectedField);
      setImgLink("");
    }
  };

  const onChangeImgLink = (e) => {
    const value = e.target.value;
    setImgLink(value);
    setImg(null);
  };

  const getASCIIByLink = async () => {
    try {
      const response = await axios.post(`${PORT}/get-txt-by-img-url`, null, {
        params: { url: imgLink }, // Move params here
        responseType: "blob",
      });

      // Create a URL for the blob response
      const url = window.URL.createObjectURL(new Blob([response.data]));

      // Create a link element to trigger the download
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "ascii.txt");
      document.body.appendChild(link);
      link.click();
      link.remove();

      toast.success("Successfully loaded");
      console.log(response.data);
    } catch (error) {
      // Check if error response exists and render a user-friendly message
      const errorMessage = error.response
        ? error.response.data.detail
        : "An unknown error occurred";
      toast.error(errorMessage);
    }
  };

  const getASCIIByImg = async () => {
    try {
      const formData = new FormData();
      formData.append("file", img); // Append the image file to the FormData

      const response = await axios.post(
        `${PORT}/get-txt-by-img-file`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data", // Set the appropriate header for file upload
          },
          responseType: "blob",
        }
      );

      // Create a URL for the blob response
      const url = window.URL.createObjectURL(new Blob([response.data]));

      // Create a link element to trigger the download
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "ascii.txt"); // Set the filename for the downloaded file
      document.body.appendChild(link);
      link.click(); // Trigger the download
      link.remove(); // Remove the link after downloading

      toast.success("Successfully loaded");
      console.log(response.data);
    } catch (error) {
      toast.error(
        "Error loading ASCII: " +
          (error.response?.data?.message || error.message)
      );
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!img && !imgLink) {
      toast.error("Please select an image or provide a link");
    } else if (img) {
      getASCIIByImg(); // Call getASCIIByImg for file upload
    } else {
      getASCIIByLink(); // Call getASCIIByLink for URL
    }
  };

  return (
    <section className={css.form__section}>
      <Toaster />
      <div className="container">
        <div className={css.form__inner}>
          <form className={css.form} onSubmit={handleSubmit}>
            <label>
              <input
                className={cn(css.form__input)}
                type="text"
                value={imgLink}
                placeholder="Image link"
                onChange={onChangeImgLink}
              />
            </label>
            <label>
              <input
                className={css.form__input__file}
                type="file"
                onChange={onChangeImg}
              />
            </label>
            <button className={css.form__btn} type="submit">
              Submit
            </button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default Form;
