const data = JSON.parse(require('fs').readFileSync('/dev/stdin', 'utf8'));

const filePath = data.tool_input?.file_path || '';

const restricted = ['.env', 'secrets.json', 'private/'];

if (restricted.some(f => filePath.includes(f))) {
  process.stderr.write('Access denied: restricted file. Claude cannot read sensitive files.');
  process.exit(2);
}

process.exit(0);