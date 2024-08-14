# FazendaTech - Programming Challenge

## 03 - React

This challenge is designed to test your knowledge of React.

### Problem 01 - Dynamic React Component

You are given a simple React component that receives a list of items.
It either renders a `No items!` message if the list is empty, or a card that displays one item at a time.

```tsx
import React, { useState } from 'react';

interface Item {
  name: string;
  description: string;
}

interface ItemsCardProps {
  items: Item[];
}

export default function ItemsCard({ items }: ItemsCardProps) {
  if (items.length === 0) {
    return <div>No items!</div>;
  }

  const [currentIndex, setCurrentIndex] = useState(0);

  const item = items[currentIndex];

  return (
    <div>
      <h3>Item #${currentIndex + 1} - {item.name}</h3>
      <span>{item.description}</span>
      <button onClick={() => setIndex(i => (i + 1) % items.length)}>Next</button>
    </div>
  );
}
```

#### Your Task

This component works, but it breaks a fundamental rule of React.

1. What is the React rule that is being broken?
2. How would you fix it?
3. Why is this rule important?


### Problem 02 - Rendering Arrays

You are given a React component which renders a list of items.

```tsx
import React from 'react';

interface Item {
  name: string;
  description: string;
}

interface ItemsListProps {
  items: Item[];
}

export default function ItemsList({ items }: ItemsListProps) {
  return (
    <div>
      {items.map(item => (
        <div>
          <h3>{item.name}</h3>
          <span>{item.description}</span>
        </div>
      ))}
    </div>
  );
}
```

#### Your Task

This component works, but it's missing an essential details that could improve its performance, specially considering the list of items can change frequently.

1. What is the missing detail?
2. How would you implement it?
3. Is there something you could add to the `Item` interface to make the solution better?
