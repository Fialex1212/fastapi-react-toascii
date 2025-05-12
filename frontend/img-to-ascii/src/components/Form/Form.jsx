import { useState } from "react";
import toast, { Toaster } from "react-hot-toast";
import { getASCIIByFile, getASCIIByLink } from "../../utils/ascii";

const Form = () => {
  const [imgLink, setImgLink] = useState("");
  const [imageUrl, setImageUrl] = useState(null);
  const [fileName, setFileName] = useState("Choise file");
  const [imgPreview, setImgPreview] = useState(null);

  const onChangeFile = (e) => {
    e.preventDefault();
    const selectedField = e.target.files[0];
    if (selectedField) {
      setImageUrl(selectedField);
      setImgLink("");
      setFileName(selectedField ? selectedField.name : "Choise file");
      const reader = new FileReader();
      reader.onloadend = () => setImgPreview(reader.result);
      reader.readAsDataURL(selectedField);
    }
  };

  const onChangeImgLink = (e) => {
    const value = e.target.value;
    setImgLink(value);
    setImageUrl(null);
    setImgPreview(value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!imageUrl && !imgLink) {
      toast.error("Please select an image or provide a link");
    } else if (imageUrl) {
      getASCIIByFile(imageUrl);
    } else {
      getASCIIByLink(imgLink);
    }
  };

  return (
    <section>
      <Toaster />
      <div className="container mx-auto">
        <div className="flex justify-center items-center h-[calc(100vh-44px)] ">
          <form
            onSubmit={handleSubmit}
            className="flex flex-col justify-center items-center row-gap-[30px] gap-[30px] px-[30px] w-full max-w-[320px] md:max-w-[400px] min-h-[440px]  bg-[var(--blocks-color)] rounded-[10px]"
          >
            {imgPreview ? (
              <>
                <div className="flex flex-col">
                  <img
                    src={imgPreview}
                    alt="Preview"
                    className="w-[200px] h-[200px] object-cover"
                  />
                  <button
                    className="cursor-pointer"
                    onClick={() => setImgPreview(null)}
                  >
                    Remove
                  </button>
                </div>
              </>
            ) : (
              <>
                <label>
                  <input
                    type="text"
                    value={imgLink}
                    onChange={onChangeImgLink}
                    placeholder="Image link"
                    className="w-[250px] h-[50px] p-[10px] border-[2px] border-blue-200 rounded-[10px] transition duration-300 hover:border-blue-200 focus:border-blue-200 outline-none"
                  />
                </label>
                <label>
                  <p
                    htmlFor="file-upload"
                    className="w-[250px] h-[50px] cursor-pointer border rounded flex items-center justify-start truncate"
                  >
                    {fileName}
                  </p>
                  <input
                    id="file-upload"
                    type="file"
                    onChange={onChangeFile}
                    className="hidden"
                  />
                </label>
              </>
            )}
            <button
              type="submit"
              className="w-[150px] h-[50px] rounded-[10px] transition duration-300 bg-blue-200 text-black hover:scale-110 hover:cursor-pointer"
            >
              Submit
            </button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default Form;
