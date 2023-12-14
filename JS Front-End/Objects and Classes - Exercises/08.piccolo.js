function manageParkingLot(input) {
    const parkingLot = new Set();
  
    input.forEach((entry) => {
      const [direction, carNumber] = entry.split(', ');
  
      if (direction === 'IN') {
        parkingLot.add(carNumber);
      } else if (direction === 'OUT') {
        parkingLot.delete(carNumber);
      }
    });
  
    const sortedCars = Array.from(parkingLot).sort();
  
    if (sortedCars.length === 0) {
      console.log('Parking Lot is Empty');
    } else {
      sortedCars.forEach((car) => {
        console.log(car);
      });
    }
  }