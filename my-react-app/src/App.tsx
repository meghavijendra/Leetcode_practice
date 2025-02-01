import ListGroup from "./components/ListGroup";

function App() {
  const cities = ["New York", "Los Angeles", "Chicago", "Houston"];
  const handleSelcted = (city: string) => {
    console.log(city);
  };
  return (
    <div>
      <ListGroup items={cities} heading="cities" onSelected={handleSelcted} />
    </div>
  );
}

export default App;
