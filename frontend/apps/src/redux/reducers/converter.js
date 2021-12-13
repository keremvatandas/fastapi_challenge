import { IMAGE_CONVERTER } from "../actions/types";

const CONVERTER_INITIAL_STATE = {
  image: "",
};

const converterReducer = (state = CONVERTER_INITIAL_STATE, action) => {
  switch (action.type) {
    case IMAGE_CONVERTER:
      return {
        ...state,
        image: action.payload,
      };

    default:
      return state;
  }
};

export default converterReducer;
