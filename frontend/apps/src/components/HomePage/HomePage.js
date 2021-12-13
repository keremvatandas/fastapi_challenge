import React, { useState } from "react";
import { Layout, Menu } from "antd";
import { categories } from "../commons/Categories";

const { Header, Content } = Layout;

const Homepage = () => {
  const [currentCategory, setCurrentCategory] = useState(categories[0]);
  return (
    <div>
      <Layout>
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
        <Content>Content</Content>
        {/* <Footer>Footer</Footer> */}
      </Layout>
    </div>
  );
};

export default Homepage;