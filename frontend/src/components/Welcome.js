import React from 'react';
import { Button } from 'react-bootstrap';

const Welcome = () => (
  <div style={{ backgroundColor: '#eeeeee' }}>
    <h1> Images Gallery</h1>
    <p>
      This is simple application that retrieve photos using Unsplash API. In
      order to start enter any search in the input field.
    </p>
    <p>
      <Button variant="primary" href="https://unsplash.com" target="_blank">
        Learn more
      </Button>
    </p>
  </div>
);

export default Welcome;
