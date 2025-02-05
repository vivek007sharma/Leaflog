import React, { useState } from 'react';
import './DropzoneArea.css';

const DropzoneArea = ({ onFileSelect, acceptedFiles = [] }) => {
  const [files, setFiles] = useState([]);

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFiles = Array.from(e.dataTransfer.files);
    const filteredFiles = droppedFiles.filter(file =>
      acceptedFiles.length === 0 || acceptedFiles.includes(file.type)
    );

    setFiles(prevFiles => [...prevFiles, ...filteredFiles]);

    if (onFileSelect) {
      onFileSelect(filteredFiles);
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleRemoveFile = (file) => {
    setFiles(files.filter(f => f !== file));
  };

  const renderFilePreview = (file) => {
    const fileUrl = URL.createObjectURL(file);
    return (
      <div className="file-preview">
        {file.type.startsWith('image/') ? (
          <img src={fileUrl} alt={file.name} className="image-preview" />
        ) : (
          <span>{file.name}</span>
        )}
        <button
          type="button"
          className="remove-file"
          onClick={() => handleRemoveFile(file)}
        >
          Remove
        </button>
      </div>
    );
  };

  return (
    <div
      className="dropzone-area"
      onDrop={handleDrop}
      onDragOver={handleDragOver}
    >
      <div className="dropzone-message">
        <p>Drag and drop files here, or click to select files</p>
      </div>
      <input
        type="file"
        multiple
        onChange={(e) => {
          const selectedFiles = Array.from(e.target.files);
          const filteredFiles = selectedFiles.filter(file =>
            acceptedFiles.length === 0 || acceptedFiles.includes(file.type)
          );
          setFiles(prevFiles => [...prevFiles, ...filteredFiles]);
          if (onFileSelect) onFileSelect(filteredFiles); // Passing the selected file back to parent component
        }}
        className="file-input"
      />
      <div className="file-list">
        {files.map((file, index) => (
          <div key={index} className="file-item">
            {renderFilePreview(file)} {/* Render the preview and the Remove button */}
          </div>
        ))}
      </div>
    </div>
  );
};

export default DropzoneArea;
