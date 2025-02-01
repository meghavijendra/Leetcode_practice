• React is a JavaScript library for building dynamic and interactive user interfaces.
• In React applications, we don’t query and update the DOM. Instead, we describe our
application using small, reusable components. React will take care of efficiently creating
and updating DOM elements.
• React components can be created using a function or a class. Function-based
components are the preferred approach as they’re more concise and easier to work
with.
• JSX stands for JavaScript XML. It is a syntax that allows us to write components that
combine HTML and JavaScript in a readable and expressive way, making it easier to
create complex user interfaces.
• When our application starts, React takes a tree of components and builds a JavaScript
data structure called the virtual DOM. This virtual DOM is different from the actual
DOM in the browser. It’s a lightweight, in-memory representation of our component
tree.
• When the state or the data of a component changes, React updates the
corresponding node in the virtual DOM to reflect the new state. Then, it compares
the current version of virtual DOM with the previous version to identify the nodes
that should be updated. It’ll then update those nodes in the actual DOM.
• In browser-based apps, updating the DOM is done by a companion library called
ReactDOM. In mobile apps, React Native uses native components to render the
user interface.
• Since React is just a library and not a framework like Angular or Vue, we often
need other tools for concerns such as routing, state management,
internationalization, form validation, etc.

• React is a popular open-source JavaScript library used for building user interfaces, particularly single-page applications where you need a fast, interactive user experience. It was developed by Facebook and is maintained by Facebook and a community of individual developers and companies.

• Key Features of React:

1. Component-Based Architecture:
   React applications are built using components, which are reusable, self-contained pieces of UI. Components can be nested, managed, and handled independently, making the development process more modular and maintainable.
2. Virtual DOM:
   React uses a virtual DOM to improve performance. The virtual DOM is a lightweight copy of the actual DOM. When the state of an object changes, React updates the virtual DOM first, then compares it with the actual DOM, and only updates the parts of the DOM that have changed. This process is called reconciliation.
3. JSX (JavaScript XML):
   JSX is a syntax extension for JavaScript that looks similar to XML or HTML. It allows developers to write HTML-like code within JavaScript, making it easier to create and visualize the structure of the UI components.
4. Unidirectional Data Flow:
   React follows a unidirectional data flow, meaning data flows in one direction from parent to child components. This makes it easier to understand and debug the application state.
5. State Management:
   React provides a way to manage the state within components. The state is an object that holds data that may change over the lifecycle of the component. React also supports state management libraries like Redux and Context API for more complex state management needs.
6. Lifecycle Methods:
   React components have lifecycle methods that allow developers to hook into different stages of a component's lifecycle, such as mounting, updating, and unmounting. These methods provide more control over the behavior of components.

• Example of a Simple React Component:
import React from 'react';

// Define a functional component
function HelloWorld() {
return (

<div>
<h1>Hello, World!</h1>
</div>
);
}

// Export the component
export default HelloWorld;

• Example of a React Component with State:
import React, { useState } from 'react';

function Counter() {
// Declare a state variable named 'count' with an initial value of 0
const [count, setCount] = useState(0);

return (

<div>
<p>You clicked {count} times</p>
<button onClick={() => setCount(count + 1)}>
Click me
</button>
</div>
);
}

export default Counter;

• In React apps, a component can only return a single element. To return multiple
elements, we wrap them in a fragment, which is represented by empty angle brackets.
• To render a list in JSX, we use the ‘array.map()’ method. When mapping items, each
item must have a unique key, which can be a string or a number.
• To conditionally render content, we can use an ‘if’ statement or a ternary operator.
• We use the state hook to define state (data that can change over time) in a component. A
hook is a function that allows us to tap into built-in features in React.
• Components can optionally have props (short for properties) to accept input.
• We can pass data and functions to a component using props. Functions are used to
notify the parent (consumer) of a component about certain events that occur in the
component, such as an item being clicked or selected.
• We should treat props as immutable (read-only) and not modify them.
• When the state or props of a component change, React will re-render the component
and update the DOM accordingly.
• In React apps, a component can only return a single element. To return multiple
elements, we wrap them in a fragment, which is represented by empty angle brackets.
• To render a list in JSX, we use the ‘array.map()’ method. When mapping items, each
item must have a unique key, which can be a string or a number.
• To conditionally render content, we can use an ‘if’ statement or a ternary operator.
• We use the state hook to define state (data that can change over time) in a component. A
hook is a function that allows us to tap into built-in features in React.
• Components can optionally have props (short for properties) to accept input.
• We can pass data and functions to a component using props. Functions are used to
notify the parent (consumer) of a component about certain events that occur in the
component, such as an item being clicked or selected.
• We should treat props as immutable (read-only) and not modify them.
• When the state or props of a component change, React will re-render the component
and update the DOM accordingly.
• The state hook allows us to add state to function components.
• Hooks can only be called at the top level of components.
• State variables, unlike local variables in a function, stay in memory as long as the
component is visible on the screen. This is because state is tied to the component
instance, and React will destroy the component and its state when it is removed from
the screen.
• React updates state in an asynchronous manner, so updates are not applied
immediately. Instead, they’re batched and applied at once after all event handlers have
finished execution. Once the state is updated, React re-renders our component.
• Group related state variables into an object to keep them organized.
• Avoid deeply nested state objects as they can be hard to update and maintain.
• To keep state as minimal as possible, avoid redundant state variables that can be
computed from existing variables.
• A pure function is one that always returns the same result given the same input. Pure
functions should not modify objects outside of the function.
• React expects our function components to be pure. A pure component should always
return the same JSX given the same input.
• To keep our components pure, we should avoid making changes during the render
phase.
• Strict mode helps us catch potential problems such as impure components. Starting
from React 18, it is enabled by default. It renders our components twice in development
mode to detect any potential side effects.
• When updating objects or arrays, we should treat them as immutable objects. Instead of
mutating them, we should create new objects or arrays to update the state.
• Immer is a library that can help us update objects and arrays in a more concise and
mutable way.
• To share state between components, we should lift the state up to the closest parent
component and pass it down as props to child components.
• The component that holds some state should be the one that updates it. If a child
component needs to update some state, it should notify the parent component using a
callback function passed down as a prop.
