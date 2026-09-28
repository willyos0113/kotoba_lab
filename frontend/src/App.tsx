import { useEffect, useState } from "react";

import { getHealth } from "./api/client";

export default function App() {
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    getHealth()
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("backend unreachable"));
  }, []);

  return (
    <main>
      <h1>Kotoba Lab</h1>
      <p>Backend status: {status}</p>
    </main>
  );
}
