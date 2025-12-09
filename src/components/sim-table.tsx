import React from 'react';

// Explicitly define the shape of a single row
interface SimRow {
  k: number;
  adds: number;
  dels: number;
  total: number;
}

// Ensure the component expects an array of these rows
export default function SimTable({ data }: { data: SimRow[] }) {
  // Safety check: If data is missing or not an array, return null to prevent crash
  if (!data || !Array.isArray(data)) {
    return <div>Error: Invalid Simulation Data</div>;
  }

  return (
    <div style={{padding: '1rem', border: '1px solid #444', borderRadius: '8px', margin: '1rem 0'}}>
      <h4 style={{margin: '0 0 1rem'}}>🛡️ Simulation Verification: Cycle Reduction</h4>
      <table style={{width: '100%', borderCollapse: 'collapse'}}>
        <thead>
          <tr style={{borderBottom: '2px solid #666'}}>
            <th style={{padding: '8px', textAlign: 'left'}}>Cycle Length (k)</th>
            <th style={{padding: '8px', textAlign: 'left'}}>Additions</th>
            <th style={{padding: '8px', textAlign: 'left'}}>Deletions</th>
            <th style={{padding: '8px', textAlign: 'left'}}>Total Steps</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, index) => (
            <tr key={row.k || index} style={{borderBottom: '1px solid #333'}}>
              {/* We explicitly render ONLY the primitive values (numbers), never the object */}
              <td style={{padding: '8px'}}>{row.k}</td>
              <td style={{padding: '8px'}}>{row.adds}</td>
              <td style={{padding: '8px'}}>{row.dels}</td>
              <td style={{padding: '8px'}}><strong>{row.total}</strong></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}