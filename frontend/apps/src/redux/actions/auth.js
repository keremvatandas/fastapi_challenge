import axios from "axios";
import { isOnline } from "../../components/commons/constants";
import { LOGIN, SET_LOGIN_SUCCESS } from "./types";

export const login = (username, password) => (dispatch) => {
  let loginUrl = `${process.env.REACT_APP_API_URL}/login`;
  axios
    .post(loginUrl, { username, password })
    .then((response) => {
      dispatch({
        type: LOGIN,
        payload: response.data.access_token,
      });
      dispatch(setLoginSuccess(true));
    })
    .catch((error) => {
      dispatch({
        type: "LOGIN_ERROR",
        payload: "Error message",
      });
    });
};

export const setLoginSuccess = (isLoginSuccess) => {
  return {
    type: SET_LOGIN_SUCCESS,
    payload: isLoginSuccess,
  };
};
