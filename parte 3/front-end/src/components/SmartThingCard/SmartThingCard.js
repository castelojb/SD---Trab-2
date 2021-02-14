import React, { useEffect, useState } from "react";
import { Card, Switch, InputNumber, Button, Progress } from "antd";
import useService from "../../hooks/useService";

const SmartThingCard = ({ id, name, type, status }) => {
  const [pageStatus, setPageStatus] = useState(status?.TURN_ON_OFF);
  const [temperature, setTemperature] = useState(status?.TEMPERATURE);
  let equipmentDetails = null;
  const { changeStatus } = useService();

  useEffect(() => {
    setPageStatus(status?.TURN_ON_OFF);
  }, [status]);

  useEffect(() => {
    changeStatus(
      id,
      Number(pageStatus),
      "TURN_ON_OFF",
      () => {},
      () => {},
      () => {}
    );
  }, [pageStatus]);

  const SaveValue = () => {
    changeStatus(
      id,
      temperature,
      "TEMPERATURE",
      () => {},
      () => {},
      () => {}
    );
  };

  if (type === "BOTH") {
    equipmentDetails = (
      <>
        <p>Sensor e atuador</p>
        {status.TURN_ON_OFF !== undefined && (
          <>
            <p>{`Equipamento está ${pageStatus ? "Ligado" : "Desligado"}`}</p>
          </>
        )}
        {status.TEMPERATURE !== undefined && (
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <InputNumber value={temperature} onChange={setTemperature} />
            <Progress
              type='circle'
              percent={status.TEMPERATURE}
              format={percert => `${percert}°C`}
              width={80}
              size='small'
            />
            <p>{`Temperatura: ${status.TEMPERATURE}°C`}</p>
          </div>
        )}
        {status.ENV_TEMPERATURE !== undefined && (
          <>
            <Progress
              type='circle'
              percent={status.TEMPERATURE}
              format={percert => `${percert}°C`}
              width={80}
              size='small'
            />

            <p>{`Temperatura no ambiente: ${status.TEMPERATURE}°C`}</p>
          </>
        )}
      </>
    );
  } else if (type === "ACTUATOR") {
    equipmentDetails = (
      <>
        <p>Atuador</p>
        {status.TURN_ON_OFF !== undefined && (
          <>
            <p>{`Equipamento está ${pageStatus ? "Ligado" : "Desligado"}`}</p>
          </>
        )}
        {status.TEMPERATURE !== undefined && (
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <InputNumber value={temperature} onChange={setTemperature} />
            <Progress
              type='circle'
              percent={status.TEMPERATURE}
              format={percert => `${percert}°C`}
              width={80}
              size='small'
            />
          </div>
        )}
      </>
    );
  } else if (type === "SENSOR") {
    equipmentDetails = (
      <>
        <p>Sensor</p>
        <Progress
          type='circle'
          percent={status.TEMPERATURE}
          format={percert => `${percert}°C`}
          width={80}
          size='small'
        />
      </>
    );
  }

  return (
    <Card
      extra={
        status.TURN_ON_OFF !== undefined &&
        type !== "SENSOR" && (
          <Switch checked={pageStatus} onChange={setPageStatus} />
        )
      }
      title={name}
      style={{
        width: 300,
        textAlign: "start",
        marginLeft: "20px",
      }}
      actions={
        type !== "SENSOR" &&
        status.TEMPERATURE && [
          <Button onClick={SaveValue}>Salvar valor</Button>,
        ]
      }
    >
      {equipmentDetails}
    </Card>
  );
};

export default SmartThingCard;
