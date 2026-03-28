const { execSync } = require('child_process');

try {
  execSync('npx tsc --noEmit', { 
    cwd: '/Users/terrencecrawford/Downloads/uigen',
    stdio: 'pipe'
  });
  process.exit(0);
} catch (error) {
  process.stderr.write('TypeScript errors found:\n' + error.stdout.toString());
  process.exit(1);
}