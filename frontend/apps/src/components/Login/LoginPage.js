import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Form, Input, Button, Row } from "antd";
import { login } from "../../redux/actions/auth";

const Loginpage = () => {
  const dispatch = useDispatch();

  const onFinish = (values) => {
    dispatch(login(values.username, values.password));
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };
  return (
    <div>
      <Row
        type="flex"
        justify="center"
        align="middle"
        style={{ minHeight: "100vh" }}
      >
        <div
          style={{
            height: "400px",
            width: "400px",
            display: "flex",
            boxShadow: "0 0 40px",
            flexDirection: "column",
          }}
        >
          <Form
            style={{
              flexDirection: "column",
              alignItems: "center",
              marginTop: "100px",
              marginRight: "50px",
            }}
            layout=""
            name="basic"
            labelCol={{
              span: 8,
            }}
            wrapperCol={{
              span: 16,
            }}
            onFinish={onFinish}
            onFinishFailed={onFinishFailed}
            autoComplete="off"
          >
            <h1 style={{ marginLeft: "80px" }}> LOGIN PAGE </h1>
            <Form.Item
              label="Username"
              name="username"
              rules={[
                {
                  required: true,
                  message: "Please input your username!",
                },
              ]}
            >
              <Input />
            </Form.Item>

            <Form.Item
              label="Password"
              name="password"
              rules={[
                {
                  required: true,
                  message: "Please input your password!",
                },
              ]}
            >
              <Input.Password />
            </Form.Item>

            <Form.Item
              wrapperCol={{
                offset: 8,
                span: 16,
              }}
            >
              <Button
                type="primary"
                htmlType="submit"
                onClick={(e) => {
                  console.log(e.target.values);
                }}
              >
                Login
              </Button>
            </Form.Item>
          </Form>
        </div>
      </Row>
    </div>
  );
};

export default Loginpage;
