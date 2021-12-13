import Apps from "../Apps/Apps";
import ImageConverter from "../ImageConverter/ImageConverter";

export const categories = [
  {
    id: 0,
    name: "Apps",
    component: <Apps />,
  },
  {
    id: 1,
    name: "Image Converter",
    component: <ImageConverter />,
  },
];
