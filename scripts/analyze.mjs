import { execSync } from 'child_process';

const result = execSync(
  'claude -p "Look at the src directory and give me a brief summary of what this project does" --output-format json',
  { 
    cwd: '/Users/terrencecrawford/Downloads/uigen',
    encoding: 'utf8'
  }
);

const parsed = JSON.parse(result);
console.log(parsed.result);
console.log(`\nCost: $${parsed.total_cost_usd.toFixed(4)}`);