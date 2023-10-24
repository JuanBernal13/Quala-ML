import React from 'react';
import { Container, Row, Col, Table } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const camionesFalsos = [
    { id: 1, nombre: 'Camión A', ruta: 'Ruta 1', productoRestante: 50, estado: 'En camino' },
    { id: 2, nombre: 'Camión B', ruta: 'Ruta 2', productoRestante: 30, estado: 'Entregando' },
    { id: 3, nombre: 'Camión C', ruta: 'Ruta 3', productoRestante: 70, estado: 'En camino' },
    // ... puedes añadir más datos falsos si lo deseas
  ];

  return (
    <Container fluid>
      <Row className="mb-4">
        <Col md={12}>
          <h1>Panel de Control de Rutas de Distribución</h1>
        </Col>
      </Row>
      <Row>
        <Col md={12}>
          <Table striped bordered hover className="mb-4">
            <thead>
              <tr>
                <th>#</th>
                <th>Camión</th>
                <th>Ruta</th>
                <th>Producto Restante</th>
                <th>Estado</th>
              </tr>
            </thead>
            <tbody>
              {camionesFalsos.map(camion => (
                <tr key={camion.id}>
                  <td>{camion.id}</td>
                  <td>{camion.nombre}</td>
                  <td>{camion.ruta}</td>
                  <td>{camion.productoRestante}</td>
                  <td>{camion.estado}</td>
                </tr>
              ))}
            </tbody>
          </Table>
          <iframe
            title="Mapa de Parqueaderos"
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3976.873782261171!2d-74.07303972398213!3d4.616595642378797!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e3f995d638ce0ad%3A0x172b873c30bd1cf8!2sAtrio!5e0!3m2!1ses-419!2sco!4v1695585497635!5m2!1ses-419!2sco"
            width="100%"
            height="450"
            style={{ border: 0 }}
            allowFullScreen=""
            loading="lazy">
          </iframe>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
