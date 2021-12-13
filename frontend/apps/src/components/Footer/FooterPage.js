import React from "react";
import { Layout } from "antd";

const { Footer } = Layout;

const FooterPage = () => {
  return (
    <Footer style={{ textAlign: "center" }}>
      {process.env.REACT_APP_FOOTER_MSG}
    </Footer>
  );
};

export default FooterPage;
