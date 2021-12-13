import React from "react";
import { Input, Button, Select } from "antd";
const { Option } = Select;
const Apps = () => {
  return (
    <div>
      <Input.Group compact>
        <Select
          style={{ width: "80%" }}
          placeholder="Type game name or select from list"
        >
          <Option value="Home">Home</Option>
          <Option value="Company">Company</Option>
        </Select>
        <Button type="primary" size="middle" style={{ marginLeft: "10px" }}>
          Randomize
        </Button>
      </Input.Group>
    </div>
  );
};

export default Apps;
