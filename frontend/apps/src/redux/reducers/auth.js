import { LOGIN, SET_LOGIN_SUCCESS } from "../actions/types";

const AUTH_INITIAL_STATE = {
  isSignedIn: false,
  access_token: "",
};

const authReducer = (state = AUTH_INITIAL_STATE, action) => {
  switch (action.type) {
    case LOGIN:
      return {
        ...state,
        access_token: action.payload,
      };
    case SET_LOGIN_SUCCESS:
      return {
        ...state,
        isSignedIn: action.payload,
      };
    default:
      return state;
  }
};

export default authReducer;
