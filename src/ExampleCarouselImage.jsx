import React from 'react';
import styles from './index.module.css';

const ExampleCarouselImage = ({ image }) => {
  return (
    <div className={styles.slide}>
       <img src={image} alt="slide" />
    </div>
  );
}

export default ExampleCarouselImage;
