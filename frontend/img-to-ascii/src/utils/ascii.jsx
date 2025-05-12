import toast from "react-hot-toast";
import { PORT } from "./constans";
import axios from "axios";

export const getASCIIByLink = async ({ imgLink }) => {
  try {
    const response = await axios.post(`${PORT}/get-txt-by-img-url`, null, {
      params: { url: imgLink },
      responseType: "blob",
    });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "ascii.txt");
    document.body.appendChild(link);
    link.click();
    link.remove();
    toast.success("Successfully loaded");
  } catch (error) {
    const errorMessage = error.response
      ? error.response.data.detail
      : "An unknown error occurred";
    toast.error(errorMessage);
  }
};

export const getASCIIByFile = async ({ imageUrl }) => {
  try {
    const formData = new FormData();
    formData.append("file", imageUrl);
    const response = await axios.post(`${PORT}/get-txt-by-img-file`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
      responseType: "blob",
    });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "ascii.txt");
    document.body.appendChild(link);
    link.click();
    link.remove();
    toast.success("Successfully loaded");
  } catch (error) {
    toast.error(
      "Error loading ASCII: " + (error.response?.data?.message || error.message)
    );
  }
};
