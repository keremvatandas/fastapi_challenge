import { combineReducers } from "redux";
import authReducer from "./auth";
import converterReducer from "./converter";

const rootReducer = combineReducers({
  auth: authReducer,
  converter: converterReducer,
});

export default rootReducer;
