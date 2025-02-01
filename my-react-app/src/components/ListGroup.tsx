import { useState } from "react";

interface ListGroupProps {
  items: string[];
  heading: string;
  onSelected: (item: string) => void;
}

function ListGroup({ items, heading, onSelected }: ListGroupProps) {
  const [selectedCity, setSelectedIndex] = useState(-1);

  return (
    <>
      <h1>{heading}</h1>
      {items.length === 0 && <p>No cities to display</p>}
      <ul className="list-group">
        {items.map((city, index) => (
          <li
            className={
              selectedCity === index
                ? "list-group-item active"
                : "list-group-item "
            }
            key={city}
            onClick={() => {
              setSelectedIndex(index);
              onSelected(city);
            }}
          >
            {city}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
