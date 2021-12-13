import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { Upload, Button } from "antd";
import { UploadOutlined } from "@ant-design/icons";
import { image_converter } from "../../redux/actions/converter";

const ImageConverter = () => {
  const accessToken = useSelector((state) => state.auth.accessToken);
  const dispatch = useDispatch();
  const upload = (file) => {
    dispatch(image_converter(file, accessToken));
  };

  return (
    <div>
      <Upload
        onChange={(file) => {
          upload(file);
        }}
      >
        <Button icon={<UploadOutlined />}>Click to Upload Image</Button>
      </Upload>
    </div>
  );
};

export default ImageConverter;
