import React, { useState, useEffect } from 'react';
import {
  Typography,
  Dialog,
  DialogTitle,
  DialogContent,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableRow,
  Paper,
  TableHead,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  List,
  ListItem,
  ListItemText,
  Divider
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { useDataProvider } from 'react-admin';
import { getConf } from '../../Config';
import { styled } from '@mui/system';

const StyledTableCell = styled(TableCell)({
  fontWeight: 'bold',
  color: '#333',
  backgroundColor: '#e0f7fa',
});

const RelatedDataInstance = ({ relatedData }) => {
  const conf = getConf();
  const resource = conf.resources && conf.resources[relatedData.type];
  if (!resource) return null;
  return (
    <List>
      {resource.attributes
        .filter((attr) => relatedData[attr.name] != null && attr.name !== 'id')
        .map((attr) => (
          <ListItem
            key={attr.name}
            style={{ padding: '2px 0', display: 'flex', justifyContent: 'space-between' }}
          >
            <ListItemText
              primary={<span><strong>{attr.label || attr.name}</strong></span>}
              style={{ width: '50%' }}
            />
            <ListItemText primary={<span>{relatedData[attr.name]}</span>} style={{ width: '50%' }} />
          </ListItem>
        ))}
    </List>
  );
};

const ResourceDialog = ({ open, onClose, resourceData, passengers }) => {
  const conf = getConf();
  const resourceConf = conf.resources && conf.resources[resourceData.type];
  if (!resourceConf) return null;

  const { attributes, tab_groups: tabGroups } = resourceConf;

  const capitalize = (str) => str.charAt(0).toUpperCase() + str.slice(1);

  const attributeItems = attributes
    .filter((attr) =>
      resourceData[attr.name] != null &&
      !['id', 'airplane_id', 'arrival_airport_id', 'departure_airport_id'].includes(attr.name)
    )
    .map((attr) => (
      <ListItem
        key={attr.name}
        style={{ padding: '2px 0', display: 'flex', justifyContent: 'space-between' }}
      >
        <ListItemText
          primary={<span><strong>{capitalize(attr.label || attr.name)}</strong></span>}
          style={{ width: '50%' }}
        />
        <ListItemText primary={<span>{resourceData[attr.name]}</span>} style={{ width: '50%' }} />
      </ListItem>
    ));

  const relatedAccordions = (tabGroups || []).map(({ name }) => {
    const relatedData = resourceData[name];
    if (!relatedData) return null;

    if (name === 'BookingList') {
      return (
        <Accordion key={name}>
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls={`panel-${name}-content`}
            id={`panel-${name}-header`}
          >
            <Typography style={{ color: '#00796b' }}>Bookings</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <TableContainer component={Paper}>
              <Table size="small">
                <TableHead>
                  <TableRow>
                    <StyledTableCell>Passenger</StyledTableCell>
                    <StyledTableCell>Seat Number</StyledTableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {relatedData.map((booking) => {
                    const passengerName = passengers[booking.passenger_id]?.name || 'Unknown';
                    return (
                      <TableRow key={booking.id}>
                        <TableCell>{passengerName}</TableCell>
                        <TableCell>{booking.seat_number || 'N/A'}</TableCell>
                      </TableRow>
                    );
                  })}
                </TableBody>
              </Table>
            </TableContainer>
          </AccordionDetails>
        </Accordion>
      );
    }

    return (
      <Accordion key={name}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls={`panel-${name}-content`}
          id={`panel-${name}-header`}
        >
          <Typography style={{ color: '#00796b' }}>{capitalize(name)}</Typography>
        </AccordionSummary>
        <AccordionDetails>
          {Array.isArray(relatedData) ? (
            <List>
              {relatedData.map((item) => (
                <RelatedDataInstance key={item.id} relatedData={item} />
              ))}
            </List>
          ) : (
            <RelatedDataInstance relatedData={relatedData} />
          )}
        </AccordionDetails>
      </Accordion>
    );
  });

  return (
    <Dialog open={open} onClose={onClose} fullWidth>
      <DialogTitle style={{ backgroundColor: '#00796b', color: '#fff' }}>
        {resourceData.flight_number || 'Resource Details'} Details
      </DialogTitle>
      <DialogContent>
        <List>
          {attributeItems}
          <ListItem style={{ padding: '2px 0', display: 'flex', justifyContent: 'space-between' }}>
            <ListItemText
              primary={<span><strong>Departure Airport</strong></span>}
              style={{ width: '50%' }}
            />
            <ListItemText
              primary={<span>{resourceData.departure_airport?.name || 'N/A'}</span>}
              style={{ width: '50%' }}
            />
          </ListItem>
          <ListItem style={{ padding: '2px 0', display: 'flex', justifyContent: 'space-between' }}>
            <ListItemText
              primary={<span><strong>Arrival Airport</strong></span>}
              style={{ width: '50%' }}
            />
            <ListItemText
              primary={<span>{resourceData.arrival_airport?.name || 'N/A'}</span>}
              style={{ width: '50%' }}
            />
          </ListItem>
        </List>
        <Divider style={{ margin: '10px 0' }} />
        {relatedAccordions}
      </DialogContent>
    </Dialog>
  );
};

const FlightTable = ({ flightData, openDialog }) => {
  const conf = getConf();
  const flightConf = conf.resources['Flight'];

  const capitalize = (str) => str.charAt(0).toUpperCase() + str.slice(1);

  return (
    <TableContainer component={Paper} style={{ backgroundColor: '#e0f2f1' }}>
      <Table aria-label="flight table">
        <TableHead>
          <TableRow>
            {flightConf.attributes.filter((attr) => attr.name !== 'id').map((attr) => (
              <StyledTableCell key={attr.name}>
                {capitalize(
                  attr.name === 'departure_airport_id'
                    ? 'Departure Airport'
                    : attr.name === 'arrival_airport_id'
                    ? 'Arrival Airport'
                    : attr.name === 'airplane_id'
                    ? 'Airplane Model'
                    : attr.label || attr.name
                )}
              </StyledTableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {flightData.map((data) => (
            <TableRow
              key={data.id}
              hover
              onClick={() => openDialog(data)}
              style={{ cursor: 'pointer' }}
            >
              {flightConf.attributes.filter((attr) => attr.name !== 'id').map((attr) => (
                <TableCell key={attr.name}>
                  {attr.name === 'departure_airport_id'
                    ? data.departure_airport?.name || 'N/A'
                    : attr.name === 'arrival_airport_id'
                    ? data.arrival_airport?.name || 'N/A'
                    : attr.name === 'airplane_id'
                    ? data.airplane?.model || 'N/A'
                    : data[attr.name] || 'N/A'}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

const LandingPage = () => {
  const dataProvider = useDataProvider();
  const [resources, setResources] = useState([]);
  const [passengers, setPassengers] = useState({});
  const [dialogData, setDialogData] = useState(null);

  useEffect(() => {
    const fetchResources = async () => {
      const conf = getConf();
      const resourceNames = Object.keys(conf.resources).filter((name) => !name.startsWith('SPA'));
      const fetchData = resourceNames.map((name) =>
        dataProvider.getList(name, {
          pagination: { page: 1, perPage: 5 },
          meta: { include: ['+all'] },
        })
      );
      const results = await Promise.all(fetchData);
      const resourceMap = resourceNames.reduce((acc, name, index) => {
        acc[name] = results[index].data;
        return acc;
      }, {});
      setResources(resourceMap);

      // Map passengers by their ID for quick lookup
      const passengersData = results[resourceNames.indexOf('Passenger')].data;
      const passengersMap = passengersData.reduce((acc, passenger) => {
        acc[passenger.id] = passenger;
        return acc;
      }, {});
      setPassengers(passengersMap);
    };
    fetchResources();
  }, [dataProvider]);

  const openDialog = (data) => {
    setDialogData(data);
  };

  const closeDialog = () => {
    setDialogData(null);
  };

  return (
    <div style={{ padding: '16px' }}>
      <Typography variant="h4" gutterBottom style={{ color: '#00796b' }}>
        Flight Overview
      </Typography>
      {resources['Flight'] && <FlightTable flightData={resources['Flight']} openDialog={openDialog} />}
      {dialogData && (
        <ResourceDialog open={!!dialogData} onClose={closeDialog} resourceData={dialogData} passengers={passengers} />
      )}
    </div>
  );
};

export default LandingPage;