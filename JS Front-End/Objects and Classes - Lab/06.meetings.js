function meetings(appointments) {
  const meetings = {};
  const successfulMeetings = [];

  for (let i = 0; i < appointments.length; i++) {
    const [day, name] = appointments[i].split(" ");
    if (meetings[day]) {
      console.log(`Conflict on ${day}!`);
    } else {
      meetings[day] = name;
      successfulMeetings.push(appointments[i]);
      console.log(`Scheduled for ${day}`);
    }
  }

  for (let j = 0; j < successfulMeetings.length; j++) {
    const [day, name] = successfulMeetings[j].split(" ");
    console.log(`${day} -> ${name}`);
  }
}