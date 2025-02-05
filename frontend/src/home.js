import { useState, useEffect } from "react";
import React from "react";
import axios from "axios";
import cblogo from "./cblogo.png";
import image from "./bg.jpg";
import DropzoneArea from "./ui/DropzoneArea";
import "./styles.css";

export const ImageUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  let confidence = 0;

  const sendFile = async () => {
    if (selectedFile) {
      let formData = new FormData();
      formData.append("file", selectedFile);
      let res = await axios.post(process.env.REACT_APP_API_URL, formData);
      if (res.status === 200) {
        setData(res.data);
      }
      setIsLoading(false);
    }
  };

  const clearData = () => {
    setData(null);
    setSelectedFile(null);
    setPreview(null);
  };

  useEffect(() => {
    if (!selectedFile) {
      setPreview(null);
      return;
    }
    const objectUrl = URL.createObjectURL(selectedFile);
    setPreview(objectUrl);
  }, [selectedFile]);

  useEffect(() => {
    if (!preview) return;
    setIsLoading(true);
    sendFile();
  }, [preview]);

  const onSelectFile = (files) => {
    if (!files || files.length === 0) {
      setSelectedFile(null);
      return;
    }
    setSelectedFile(files[0]);
    setData(null);
  };

  const removeFile = () => {
    setSelectedFile(null);
    setPreview(null);
  };

  if (data) {
    confidence = (parseFloat(data.confidence) * 100).toFixed(2);
  }

  return (
    <div className="container">
      <header className="appbar">
        <p id="main-title">LeafLog: Leaves Classification</p>
        <img src={cblogo} alt="Logo" className="logo" />
      </header>
      <main className="main-container" style={{ backgroundImage: `url(${image})` }}>
        <div className="image-card">
          {selectedFile ? (
            <div className="remove-image-button">
              <img src={preview} alt="Uploaded" className="uploaded-image" />
              <button onClick={removeFile}>Remove Image</button>
            </div>
          ) : (
            <DropzoneArea onFileSelect={onSelectFile} />
          )}
        </div>
      </main>
    </div>
  );
};

export default ImageUpload