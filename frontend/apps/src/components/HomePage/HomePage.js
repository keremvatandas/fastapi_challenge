import React, { useState } from "react";
import { Layout, Menu } from "antd";
import { categories } from "../commons/Categories";
import FooterPage from "../Footer/FooterPage";

const { Header, Content } = Layout;

const Homepage = () => {
  const [currentCategory, setCurrentCategory] = useState(categories[0]);
  return (
    <div>
      <Layout style={{ minHeight: "100vh" }}>
        <Header>
          <Menu
            mode="horizontal"
            theme="dark"
            defaultSelectedKeys={["0"]}
            onClick={(cat) => {
              setCurrentCategory(categories[cat.key]);
            }}
            style={{ height: "100%", borderRight: 0 }}
          >
            {categories.map((cat) => {
              return <Menu.Item key={cat.id}>{cat.name}</Menu.Item>;
            })}
          </Menu>
        </Header>
        <Layout>
          <Layout style={{ padding: "0 24px 24px" }}>
            <Content
              className="site-layout-background"
              style={{
                padding: 24,
                margin: 0,
                minHeight: 280,
              }}
            >
              {currentCategory?.component}
            </Content>
          </Layout>
        </Layout>
        <FooterPage />
      </Layout>
    </div>
  );
};

export default Homepage;
