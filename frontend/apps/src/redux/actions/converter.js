import axios from "axios";
import { IMAGE_CONVERTER } from "./types";

export const image_converter = (file, accessToken) => (dispatch) => {
  let converterUrl = `${process.env.REACT_APP_API_URL}/converter`;
  try {
    console.log("Upload Image", file);
    const formData = new FormData();
    formData.append("file", file.filename);
    const config = {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    };

    axios.post(converterUrl, formData, config).then((response) => {
      dispatch({
        type: IMAGE_CONVERTER,
        payload: response.data,
      });
    });
  } catch (error) {
    console.error(error);
  }
};
