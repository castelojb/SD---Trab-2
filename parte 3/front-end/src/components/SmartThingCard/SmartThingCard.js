import React, { useEffect, useState } from "react";
import { Card, Switch, InputNumber, Button } from "antd";
import useService from "../../hooks/useService";

const SmartThingCard = ({ id, name, type, status }) => {
  const [pageStatus, setPageStatus] = useState(status?.TURN_ON_OFF);
  const [temperature, setTemperature] = useState(status?.TEMPERATURE);
  let equipmentDetails = null;
  const { changeStatus } = useService();

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
            <Switch checked={pageStatus} onChange={setPageStatus} />
            <p>{`Equipamento está ${status === 1 ? "Ligado" : "Desligado"}`}</p>
          </>
        )}
        {status.TEMPERATURE !== undefined && (
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <InputNumber value={temperature} onChange={setTemperature} />
            <p>{`Temperatura: ${status.TEMPERATURE}°C`}</p>
          </div>
        )}
        {status.ENV_TEMPERATURE !== undefined && (
          <p>{`Temperatura no ambiente: ${status.TEMPERATURE}°C`}</p>
        )}
      </>
    );
  } else if (type === "ACTUATOR") {
    equipmentDetails = (
      <>
        <p>Atuador</p>
        {status.TURN_ON_OFF !== undefined && (
          <>
            <Switch checked={pageStatus} onChange={setPageStatus} />
            <p>{`Equipamento está ${status === 1 ? "Ligado" : "Desligado"}`}</p>
          </>
        )}
        {status.TEMPERATURE !== undefined && (
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <InputNumber value={temperature} onChange={setTemperature} />
            <p>{`Temperatura: ${status.TEMPERATURE}°C`}</p>
          </div>
        )}
      </>
    );
  } else if (type === "SENSOR") {
    equipmentDetails = (
      <>
        <p>Sensor</p>
        <p>{`Temperatura: ${status.TEMPERATURE}°C`}</p>
      </>
    );
  }

  return (
    <Card
      title={name}
      style={{
        width: 300,
        textAlign: "start",
        marginLeft: "20px",
      }}
      actions={[<Button onClick={SaveValue}>Salvar valor</Button>]}
    >
      {equipmentDetails}
    </Card>
  );
};

export default SmartThingCard;
