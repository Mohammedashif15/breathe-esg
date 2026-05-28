import React, { useState } from "react";
import API from "../services/api";

function UploadForm() {

  const [file, setFile] = useState(null);
  const [sourceType, setSourceType] = useState("SAP");
  const [message, setMessage] = useState("");
  const [fileName, setFileName] = useState("");

  const handleFileChange = (e) => {

    const selectedFile = e.target.files[0];

    if (selectedFile) {

      setFile(selectedFile);
      setFileName(selectedFile.name);

    } else {

      setFile(null);
      setFileName("");
    }
  };

  const handleUpload = async (e) => {

    e.preventDefault();

    if (!file) {

      setMessage("Please select file");
      return;
    }

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    formData.append(
      "source_type",
      sourceType
    );

    try {

      const response = await API.post(
        "/ingestion/upload/",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

      setMessage(
        response.data.message
      );

    } catch (error) {

      console.log(error);

      if (
        error.response &&
        error.response.data
      ) {

        setMessage(
          error.response.data.error
        );

      } else {

        setMessage(
          "Upload failed"
        );
      }
    }
  };

  return (

    <div
      style={{
        border: "1px solid #ccc",
        padding: "20px",
        width: "420px",
        borderRadius: "10px",
      }}
    >

      <h2>Upload ESG CSV</h2>

      <label>
        Source Type
      </label>

      <br /><br />

      <select
        value={sourceType}
        onChange={(e) =>
          setSourceType(
            e.target.value
          )
        }
      >
        <option value="SAP">
          SAP
        </option>

        <option value="UTILITY">
          UTILITY
        </option>

        <option value="TRAVEL">
          TRAVEL
        </option>
      </select>

      <br /><br />

      <input
        type="file"
        accept="*"
        onChange={handleFileChange}
      />

      <br /><br />

      <p>

        Selected File:

        {" "}

        {fileName || "No file selected"}

      </p>

      <button
        onClick={handleUpload}
      >
        Upload CSV
      </button>

      <br /><br />

      <p>{message}</p>

    </div>
  );
}

export default UploadForm;