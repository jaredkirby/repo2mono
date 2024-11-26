# Project Analysis
Project Type: nextjs

## Project Configuration:
### Custom Exclusions:
- data

## Key Directories:
Important directories for this project type:
- public/
- lib/

## Configuration Files:
- package.json
- tsconfig.json

## Table of Contents

- [LICENSE.md](#Usersjaredkirbyllm_projectscampaignreportgeneratorLICENSEmd)
- [next-env.d.ts](#Usersjaredkirbyllm_projectscampaignreportgeneratornextenvdts)
- [README.md](#Usersjaredkirbyllm_projectscampaignreportgeneratorREADMEmd)
- [tailwind.config.ts](#Usersjaredkirbyllm_projectscampaignreportgeneratortailwindconfigts)
- [package.json](#Usersjaredkirbyllm_projectscampaignreportgeneratorpackagejson)
- [tsconfig.json](#Usersjaredkirbyllm_projectscampaignreportgeneratortsconfigjson)
- [next.config.ts](#Usersjaredkirbyllm_projectscampaignreportgeneratornextconfigts)
- [processCampaigns.js](#Usersjaredkirbyllm_projectscampaignreportgeneratorscriptsprocessCampaignsjs)
- [build.js](#Usersjaredkirbyllm_projectscampaignreportgeneratorscriptsbuildjs)
- [campaignProcessor.js](#Usersjaredkirbyllm_projectscampaignreportgeneratorlibcampaignProcessorjs)
- [middleware.ts](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrcmiddlewarets)
- [api.ts](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrctypesapits)
- [layout.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrcapplayouttsx)
- [page.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrcapppagetsx)
- [globals.css](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrcappglobalscss)
- [route.ts](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrcappapireporttypefilenameroutets)
- [route.ts](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrcappapiprocessroutets)
- [campaign-report-processor.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentscampaignreportprocessortsx)
- [tabs.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuitabstsx)
- [card.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuicardtsx)
- [progress.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuiprogresstsx)
- [scroll-area.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuiscrollareatsx)
- [label.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuilabeltsx)
- [alert.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuialerttsx)
- [badge.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuibadgetsx)
- [separator.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuiseparatortsx)
- [button.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuibuttontsx)
- [input.tsx](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuiinputtsx)
- [utils.ts](#Usersjaredkirbyllm_projectscampaignreportgeneratorsrclibutilsts)

## Codebase Architecture

```
campaign-report-generator
├── LICENSE.md
├── README.md
├── data/
    ├── config/
    ├── history/
    ├── output/
    ├── uploads/
├── lib/
    ├── campaignProcessor.js
├── next-env.d.ts
├── next.config.ts
├── package.json
├── public/
├── scripts/
    ├── build.js
    ├── processCampaigns.js
├── src/
    ├── app/
        ├── api/
            ├── process/
                ├── route.ts
            ├── report/
                ├── [type]/
                    ├── [filename]/
                        ├── route.ts
        ├── fonts/
        ├── globals.css
        ├── layout.tsx
        ├── page.tsx
    ├── components/
        ├── campaign-report-processor.tsx
        ├── ui/
            ├── alert.tsx
            ├── badge.tsx
            ├── button.tsx
            ├── card.tsx
            ├── input.tsx
            ├── label.tsx
            ├── progress.tsx
            ├── scroll-area.tsx
            ├── separator.tsx
            ├── tabs.tsx
    ├── lib/
        ├── utils.ts
    ├── middleware.ts
    ├── types/
        ├── api.ts
├── tailwind.config.ts
├── tsconfig.json
```

## File: LICENSE.md
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorLICENSEmd'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/LICENSE.md

```markdown
MIT License

Copyright (c) 2024 Jared Kirby

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: next-env.d.ts
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratornextenvdts'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/next-env.d.ts

```typescript
/// <reference types="next" />
/// <reference types="next/image-types/global" />

// NOTE: This file should not be edited
// see https://nextjs.org/docs/app/building-your-application/configuring/typescript for more information.

```

## File: README.md
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorREADMEmd'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/README.md

```markdown
# Campaign Report Generator

A Python-based tool that generates formatted Markdown and email reports for tracking media campaign status across different retailers. The tool tracks changes between report generations, highlights new campaigns, organizes campaigns by their current status, and can automatically distribute reports via email.

## Features

- Automatically categorizes campaigns into active, upcoming, and completed
- Organizes upcoming campaigns by month for better planning
- Tracks and highlights changes between report generations
- Maintains historical versions of campaign data
- Generates both Markdown reports and email-friendly formats
- Shows budget allocations at campaign, retailer, and monthly levels
- Includes campaign status checklists for setup tracking
- Automated email distribution of reports
- Automatic cleanup of old report files

## Prerequisites

- Python 3.8+
- pandas
- pyyaml
- python-dotenv

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jaredkirby/campaign-report-generator.git
cd campaign-report-generator
```

2. Install required packages:
```bash
pip install pandas pyyaml python-dotenv
```

## Configuration

### Basic Configuration
Create a `config.yaml` file in the project directory:

```yaml
input_offsite_csv: "path/to/your/input.csv"
output_dir: "path/to/output/directory"
```

### Email Configuration
Create a `.env` file in the project directory with your email settings:

```env
EMAIL_SMTP_SERVER=smtp.office365.com
EMAIL_SMTP_PORT=587
EMAIL_SENDER=your-email@example.com
EMAIL_SENDER_PASSWORD=your-password
EMAIL_PRIMARY_RECIPIENTS=recipient1@example.com,recipient2@example.com
EMAIL_CC_RECIPIENTS=cc1@example.com,cc2@example.com
```

Create **`reports`** and **`output`** directories in the project directory to store the input files and generated outputs, respectively.

## Input File Format

The tool expects a CSV file with the following columns:

- Tactic Start Date
- Tactic End Date
- Tactic Vendor
- Retailer
- Tactic Brand
- Event Name
- Tactic Name
- Tactic Product
- Tactic Order ID
- Tactic Allocated Budget

> **Note**: Use the Report Engine in Shopperations to generate a properly formatted CSV file.

Example CSV format:
```csv
"Tactic Start Date","Tactic End Date","Retailer","Tactic Brand","Event Name","Tactic Name","Tactic Vendor","Tactic Product","Budget Type","Tactic Order ID","Tactic Allocated Budget"
"2024-01-01","2024-01-31","ExampleRetailer","BrandName","EventName","CampaignType","VendorName","ProductName","Working","12345-01","50000"
```

## Usage

Run the script:
```bash
python campaign_report.py --config config.yaml
```

The tool will:
1. Read the input CSV file
2. Compare with previous report data (if any)
3. Generate both Markdown and email-friendly reports
4. Save a versioned copy of the campaign data for future change tracking
5. Send email reports if configured
6. Clean up old report files (configurable retention period)

## Output

The tool generates three types of files:

1. Campaign Status Report (`Campaign_Status_Report_YYYYMMDD_HHMMSS.md`):
   - Summary of all campaigns
   - Budget totals
   - Campaign details grouped by status and retailer
   - Monthly organization for upcoming campaigns
   - Change indicators for modified campaigns

2. Email Report (`Campaign_Status_Email_YYYYMMDD_HHMMSS.txt`):
   - Email-friendly text format of the campaign status
   - Same organization as the Markdown report
   - Optimized for email reading

3. Historical Data (`campaign_history/campaign_history_YYYYMMDD_HHMMSS.json`):
   - Versioned snapshots of campaign data
   - Used for change tracking between reports

### Change Indicators

The report uses the following indicators:
- ⚠️ Campaign has changes
- 🆕 New campaign
- 🔄 Number of changes in section

## Report Sections

Each report includes:
1. Summary statistics
2. Currently Active Campaigns (grouped by retailer)
3. Upcoming Campaigns (grouped by month, then retailer)
4. Completed Campaigns (grouped by retailer)

Each campaign entry shows:
- Event details
- Product information
- Budget allocation
- Date range
- Vendor information
- Setup status checklist
- Change history (if applicable)

## Email Distribution

When email configuration is present, the tool will:
- Send reports to specified primary recipients
- CC additional stakeholders as configured
- Include the report content in the email body
- Attach the Markdown version for reference
- Use a standardized subject line with the report date

## Report Cleanup

The tool automatically manages report history:
- Keeps reports for a configurable number of days (default: 30)
- Automatically removes older report files
- Maintains a clean output directory
- Preserves historical data for change tracking

## Troubleshooting

Common issues:
1. Missing columns in input CSV:
   - Ensure all required columns are present
   - Check column names match exactly

2. Date format issues:
   - Dates should be in YYYY-MM-DD format
   - Remove any summary or total rows

3. Budget format issues:
   - Budget values should be numbers
   - Remove any currency symbols or commas

4. Email configuration issues:
   - Verify SMTP settings
   - Check email credentials
   - Ensure recipient addresses are valid
   - Check firewall/security settings

## Improvement TODOs
   - Create separate modules:
      - config.py - Configuration handling
      - data_processing.py - Data loading and processing
      - report_generators.py - Report generation logic
      - email_handler.py - Email functionality
      - utils.py - Shared utilities
   - Separate constants to congif file.
   - Improve error handling and logging.
   - Add context managers for file operations and resource handling.
   - Add more specific type hints using TypeVar and Protocol.
   - Use dataclasses for data containers.
   - Replace string concatenation with f-strings.
   - Add unit tests for core functions.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

## File: tailwind.config.ts
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratortailwindconfigts'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/tailwind.config.ts

```typescript
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./src/**/*.{ts,tsx}",
  ],
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: 0 },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: 0 },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  plugins: [require("tailwindcss-animate"), require("@tailwindcss/typography")],
};

```

## File: package.json
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorpackagejson'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/package.json

```json
{
  "name": "campaign-report-generator",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "start": "next start",
    "lint": "next lint",
    "build": "next build",
    "process-campaigns": "node scripts/processCampaigns.js"
  },
  "dependencies": {
    "@radix-ui/react-label": "^2.1.0",
    "@radix-ui/react-progress": "^1.1.0",
    "@radix-ui/react-scroll-area": "^1.2.0",
    "@radix-ui/react-separator": "^1.1.0",
    "@radix-ui/react-slot": "^1.1.0",
    "@radix-ui/react-tabs": "^1.1.1",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.1.1",
    "csv-parse": "^5.5.3",
    "date-fns": "^3.3.1",
    "lucide-react": "^0.456.0",
    "next": "14.2.17",
    "nodemailer": "^6.9.9",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "react-markdown": "^9.0.1",
    "tailwind-merge": "^2.5.4",
    "tailwindcss-animate": "^1.0.7",
    "yaml": "^2.6.0"
  },
  "devDependencies": {
    "@tailwindcss/typography": "^0.5.15",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "postcss": "^8",
    "tailwindcss": "^3.4.1",
    "typescript": "^5"
  },
  "overrides": {
    "next": "14.2.17",
    "react": "18.2.0",
    "react-dom": "18.2.0"
  }
}
```

## File: tsconfig.json
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratortsconfigjson'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts", "scripts/processCampaigns.js"],
  "exclude": ["node_modules"]
}

```

## File: next.config.ts
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratornextconfigts'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/next.config.ts

```typescript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  experimental: {
    serverComponentsExternalPackages: ['python-shell'],
  },
  // Add headers to allow file uploads
  async headers() {
    return [
      {
        source: '/api/:path*',
        headers: [
          {
            key: 'Cache-Control',
            value: 'no-store, must-revalidate',
          },
        ],
      },
    ];
  },
}

module.exports = nextConfig
```

## File: processCampaigns.js
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorscriptsprocessCampaignsjs'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/scripts/processCampaigns.js

```javascript
const path = require('path');
const CampaignProcessor = require('../lib/campaignProcessor');

async function main() {
  const config = {
    inputPath: path.join(process.cwd(), 'data', 'uploads', 'current.csv'),
    historyPath: path.join(process.cwd(), 'data', 'history', 'latest.json'),
    markdownPath: path.join(process.cwd(), 'data', 'output', `report_${Date.now()}.md`),
    textPath: path.join(process.cwd(), 'data', 'output', `report_${Date.now()}.txt`),
  };

  const processor = new CampaignProcessor(config);
  const result = await processor.process();

  if (result.success) {
    console.log('Processing completed successfully');
    console.log(`Processed ${result.campaignCount} campaigns`);
    console.log(`Detected ${result.changesDetected} changes`);
    console.log('Reports generated at:');
    console.log(`- Markdown: ${result.reportPaths.markdown}`);
    console.log(`- Text: ${result.reportPaths.text}`);
  } else {
    console.error('Processing failed:', result.error);
    process.exit(1);
  }
}

main().catch(error => {
  console.error('Unexpected error:', error);
  process.exit(1);
});
```

## File: build.js
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorscriptsbuildjs'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/scripts/build.js

```javascript
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

// Ensure Python environment is set up
try {
  // Create data directories
  const dirs = ['uploads', 'output', 'history', 'config'].map(dir => 
    path.join(process.cwd(), 'data', dir)
  );
  
  dirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
  });

  // Check if we're in Vercel environment
  if (process.env.VERCEL) {
    console.log('Installing Python in Vercel environment...');
    // Use Python from Vercel runtime
    execSync('python3.11 -m ensurepip', { stdio: 'inherit' });
    execSync('python3.11 -m pip install --upgrade pip', { stdio: 'inherit' });
    execSync('python3.11 -m pip install -r requirements.txt', { stdio: 'inherit' });
  } else {
    // Local development environment
    console.log('Installing Python dependencies...');
    execSync('pip install -r requirements.txt', { stdio: 'inherit' });
  }
} catch (error) {
  console.error('Error during build:', error);
  process.exit(1);
}
```

## File: campaignProcessor.js
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorlibcampaignProcessorjs'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/lib/campaignProcessor.js

```javascript
const { parse } = require("csv-parse/sync");
const { format, parseISO, isAfter, isBefore, isEqual } = require("date-fns");
const crypto = require("crypto");
const fs = require("fs").promises;
const path = require("path");

class CampaignProcessor {
  constructor(config) {
    this.config = config;
    this.dateFormat = "yyyy-MM-dd";
  }

  async readCSV(filePath) {
    const fileContent = await fs.readFile(filePath, "utf-8");
    return parse(fileContent, {
      columns: true,
      skip_empty_lines: true,
      trim: true,
    });
  }

  validateData(data) {
    const requiredColumns = [
      "Tactic Start Date",
      "Tactic End Date",
      "Tactic Vendor",
      "Retailer",
      "Tactic Brand",
      "Event Name",
      "Tactic Name",
      "Tactic Description",
      "Tactic Product",
      "Tactic Order ID",
      "Event ID",
      "Tactic Allocated Budget",
    ];

    const missingColumns = requiredColumns.filter(
      (col) => !data[0] || !(col in data[0])
    );

    if (missingColumns.length > 0) {
      throw new Error(`Missing required columns: ${missingColumns.join(", ")}`);
    }
  }

  formatCurrency(amount) {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: "USD",
      minimumFractionDigits: 2,
    }).format(amount);
  }

  generateCampaignHash(campaign) {
    const keyFields = [
      campaign["Tactic Order ID"],
      campaign.Retailer,
      campaign["Tactic Brand"],
      campaign["Event Name"],
    ];
    return crypto.createHash("md5").update(keyFields.join("|")).digest("hex");
  }

  categorizeCampaigns(campaigns) {
    const now = new Date();

    return campaigns.reduce(
      (acc, campaign) => {
        const startDate = parseISO(campaign["Tactic Start Date"]);
        const endDate = parseISO(campaign["Tactic End Date"]);

        if (isAfter(startDate, now)) {
          acc.future.push(campaign);
        } else if (isBefore(endDate, now)) {
          acc.past.push(campaign);
        } else {
          acc.current.push(campaign);
        }

        return acc;
      },
      { current: [], future: [], past: [] }
    );
  }

  compareValues(current, historical, field) {
    if (field.includes("Date")) {
      return (
        format(parseISO(current), this.dateFormat) ===
        format(parseISO(historical), this.dateFormat)
      );
    }
    if (field === "Tactic Allocated Budget") {
      return parseFloat(current) === parseFloat(historical);
    }
    return current === historical;
  }

  findChanges(campaigns, historicalData) {
    const monitoredFields = [
      "Tactic Allocated Budget",
      "Tactic Start Date",
      "Tactic End Date",
      "Tactic Vendor",
      "Tactic Product",
    ];

    return campaigns.map((campaign) => {
      const hash = this.generateCampaignHash(campaign);
      const historical = historicalData?.find(
        (h) => this.generateCampaignHash(h) === hash
      );

      if (!historical) {
        return { ...campaign, changes: ["New Campaign"] };
      }

      const changes = monitoredFields
        .filter(
          (field) =>
            !this.compareValues(campaign[field], historical[field], field)
        )
        .map((field) => {
          if (field === "Tactic Allocated Budget") {
            const currentAmount = parseFloat(campaign[field]);
            const historicalAmount = parseFloat(historical[field]);
            const diff = currentAmount - historicalAmount;
            return `Budget changed from ${this.formatCurrency(
              historicalAmount
            )} to ${this.formatCurrency(currentAmount)} (${
              diff >= 0 ? "+" : ""
            }${this.formatCurrency(diff)})`;
          }
          if (field.includes("Date")) {
            return `${field.replace("Tactic ", "")} changed from ${format(
              parseISO(historical[field]),
              this.dateFormat
            )} to ${format(parseISO(campaign[field]), this.dateFormat)}`;
          }
          return `${field.replace("Tactic ", "")} changed from '${
            historical[field]
          }' to '${campaign[field]}'`;
        });

      return { ...campaign, changes };
    });
  }

  async loadHistoricalData() {
    try {
      const data = await fs.readFile(this.config.historyPath, "utf-8");
      return JSON.parse(data);
    } catch (error) {
      return [];
    }
  }

  async saveHistoricalData(data) {
    await fs.writeFile(this.config.historyPath, JSON.stringify(data, null, 2));
  }

  async process() {
    try {
      // Read and validate current data
      const campaigns = await this.readCSV(this.config.inputPath);
      this.validateData(campaigns);

      // Load historical data and find changes
      const historicalData = await this.loadHistoricalData();
      const processedCampaigns = this.findChanges(campaigns, historicalData);

      // Save current data as historical
      await this.saveHistoricalData(processedCampaigns);

      // Generate reports
      const { markdown, text } = this.generateReports(processedCampaigns);

      // Save reports
      await fs.writeFile(this.config.markdownPath, markdown);
      await fs.writeFile(this.config.textPath, text);

      return {
        success: true,
        campaignCount: processedCampaigns.length,
        changesDetected: processedCampaigns.filter((c) => c.changes?.length > 0)
          .length,
        reportPaths: {
          markdown: this.config.markdownPath,
          text: this.config.textPath,
        },
      };
    } catch (error) {
      return {
        success: false,
        error: error.message,
      };
    }
  }

  generateReports(campaigns) {
    const { current, future, past } = this.categorizeCampaigns(campaigns);
    const totalBudget = campaigns.reduce(
      (sum, c) => sum + parseFloat(c["Tactic Allocated Budget"]),
      0
    );

    const changedCampaigns = campaigns.filter(
      (c) => c.changes?.length > 0 && !c.changes.includes("New Campaign")
    ).length;

    const newCampaigns = campaigns.filter((c) =>
      c.changes?.includes("New Campaign")
    ).length;

    const reportDate = format(new Date(), this.dateFormat);

    // Generate both markdown and text versions
    const markdown = this.generateMarkdownReport({
      current,
      future,
      past,
      totalBudget,
      changedCampaigns,
      newCampaigns,
      reportDate,
    });

    const text = this.generateTextReport({
      current,
      future,
      past,
      totalBudget,
      changedCampaigns,
      newCampaigns,
      reportDate,
    });

    return { markdown, text };
  }

  generateMarkdownReport({
    current,
    future,
    past,
    totalBudget,
    changedCampaigns,
    newCampaigns,
    reportDate,
  }) {
    const sections = [];

    // Header
    sections.push(`# Campaign Status Report - ${reportDate}\n`, "## Summary\n");

    // Summary section
    sections.push(
      `- Total Budget: ${this.formatCurrency(totalBudget)}`,
      `- Total Campaigns: ${current.length + future.length + past.length}`,
      `- Currently Active: ${current.length}`,
      `- Upcoming: ${future.length}`,
      `- Completed: ${past.length}`,
      changedCampaigns > 0 ? `- Changed Campaigns: ${changedCampaigns}` : "",
      newCampaigns > 0 ? `- New Campaigns: ${newCampaigns}` : "",
      "\n---\n"
    );

    // Current Campaigns
    sections.push(
      "## Currently Active Campaigns\n",
      this.formatMarkdownCampaignSection(current, "current"),
      "\n---\n"
    );

    // Future Campaigns (grouped by month)
    sections.push(
      "## Upcoming Campaigns\n",
      this.formatMarkdownFutureCampaigns(future),
      "\n---\n"
    );

    // Past Campaigns
    sections.push(
      "## Completed Campaigns\n",
      this.formatMarkdownCampaignSection(past, "past"),
      "\n"
    );

    return sections.filter(Boolean).join("\n");
  }

  formatMarkdownCampaignSection(campaigns, type) {
    if (campaigns.length === 0) {
      return "*No campaigns in this category.*\n";
    }

    // Group by retailer
    const byRetailer = campaigns.reduce((acc, campaign) => {
      const retailer = campaign.Retailer;
      if (!acc[retailer]) acc[retailer] = [];
      acc[retailer].push(campaign);
      return acc;
    }, {});

    const sections = [];

    for (const [retailer, retailerCampaigns] of Object.entries(byRetailer)) {
      const retailerBudget = retailerCampaigns.reduce(
        (sum, c) => sum + parseFloat(c["Tactic Allocated Budget"]),
        0
      );

      sections.push(
        `### ${retailer} (${this.formatCurrency(retailerBudget)})\n`
      );

      retailerCampaigns.forEach((campaign) => {
        sections.push(this.formatMarkdownCampaign(campaign));
      });
    }

    return sections.join("\n");
  }

  formatMarkdownFutureCampaigns(campaigns) {
    if (campaigns.length === 0) {
      return "*No upcoming campaigns.*\n";
    }

    // Group by month
    const byMonth = campaigns.reduce((acc, campaign) => {
      const month = format(
        parseISO(campaign["Tactic Start Date"]),
        "MMMM yyyy"
      );
      if (!acc[month]) acc[month] = [];
      acc[month].push(campaign);
      return acc;
    }, {});

    const sections = [];

    for (const [month, monthCampaigns] of Object.entries(byMonth)) {
      const monthBudget = monthCampaigns.reduce(
        (sum, c) => sum + parseFloat(c["Tactic Allocated Budget"]),
        0
      );

      sections.push(`### ${month} (${this.formatCurrency(monthBudget)})\n`);

      // Sub-group by retailer
      const byRetailer = monthCampaigns.reduce((acc, campaign) => {
        const retailer = campaign.Retailer;
        if (!acc[retailer]) acc[retailer] = [];
        acc[retailer].push(campaign);
        return acc;
      }, {});

      for (const [retailer, retailerCampaigns] of Object.entries(byRetailer)) {
        const retailerBudget = retailerCampaigns.reduce(
          (sum, c) => sum + parseFloat(c["Tactic Allocated Budget"]),
          0
        );

        sections.push(
          `#### ${retailer} (${this.formatCurrency(retailerBudget)})\n`
        );

        retailerCampaigns.forEach((campaign) => {
          sections.push(this.formatMarkdownCampaign(campaign));
        });
      }
    }

    return sections.join("\n");
  }

  formatMarkdownCampaign(campaign) {
    const sections = [];
    const isNew = campaign.changes?.includes("New Campaign");
    const hasChanges = campaign.changes?.length > 0 && !isNew;

    // Campaign header with change indicators
    sections.push(
      `#### ${campaign["Tactic Brand"]} ${isNew ? "🆕" : ""} ${
        hasChanges ? "⚠️" : ""
      }\n`
    );

    // Campaign details
    sections.push(
      `- **Event:** ${campaign["Event Name"]}`,
      `- **Event ID:** [${campaign["Event ID"]}](https://cemm-ajinomoto.shopperationsapp.com/events/${campaign["Event ID"]}/spend)`,
      `- **Product:** ${campaign["Tactic Product"]}`,
      `- **Campaign:** ${campaign["Tactic Name"]}`,
      campaign["Tactic Description"]
        ? `- **Description:** ${campaign["Tactic Description"]}`
        : null,
      campaign["Tactic Vendor"]
        ? `- **Vendor:** ${campaign["Tactic Vendor"]}`
        : null,
      `- **Dates:** ${format(
        parseISO(campaign["Tactic Start Date"]),
        this.dateFormat
      )} to ${format(parseISO(campaign["Tactic End Date"]), this.dateFormat)}`,
      `- **Budget:** ${this.formatCurrency(
        parseFloat(campaign["Tactic Allocated Budget"])
      )}`,
      `- **Order ID:** ${campaign["Tactic Order ID"]}`
    );

    // Changes section
    if (hasChanges) {
      sections.push(
        "\n**Changes:**",
        ...campaign.changes.map((change) => `- ${change}`)
      );
    }

    // Checklist
    sections.push(
      "\n**Checklist:**",
      "- [ ] Campaign Setup Complete",
      "- [ ] Creative Assets Received",
      "- [ ] Campaign Launch Verified",
      "\n"
    );

    return sections.filter(Boolean).join("\n");
  }

  generateTextReport({
    current,
    future,
    past,
    totalBudget,
    changedCampaigns,
    newCampaigns,
    reportDate,
  }) {
    const sections = [];

    // Header
    sections.push(
      `Campaign Status Report - ${reportDate}`,
      "=".repeat(80),
      "",
      "SUMMARY",
      "-".repeat(7),
      `Total Budget: ${this.formatCurrency(totalBudget)}`,
      `Total Campaigns: ${current.length + future.length + past.length}`,
      `Currently Active: ${current.length}`,
      `Upcoming: ${future.length}`,
      `Completed: ${past.length}`,
      changedCampaigns > 0 ? `Changed Campaigns: ${changedCampaigns}` : "",
      newCampaigns > 0 ? `New Campaigns: ${newCampaigns}` : "",
      "",
      "=".repeat(80),
      ""
    );

    // Current Campaigns
    sections.push(
      "CURRENTLY ACTIVE CAMPAIGNS",
      this.formatTextCampaignSection(current),
      "-".repeat(80),
      ""
    );

    // Future Campaigns
    sections.push(
      "UPCOMING CAMPAIGNS",
      this.formatTextFutureCampaigns(future),
      "-".repeat(80),
      ""
    );

    // Past Campaigns
    sections.push(
      "COMPLETED CAMPAIGNS",
      this.formatTextCampaignSection(past),
      ""
    );

    return sections.filter(Boolean).join("\n");
  }

  formatTextCampaignSection(campaigns) {
    if (campaigns.length === 0) {
      return "\nNo campaigns in this category.\n";
    }

    const sections = [];

    // Group by retailer
    const byRetailer = campaigns.reduce((acc, campaign) => {
      const retailer = campaign.Retailer;
      if (!acc[retailer]) acc[retailer] = [];
      acc[retailer].push(campaign);
      return acc;
    }, {});

    for (const [retailer, retailerCampaigns] of Object.entries(byRetailer)) {
      const retailerBudget = retailerCampaigns.reduce(
        (sum, c) => sum + parseFloat(c["Tactic Allocated Budget"]),
        0
      );

      sections.push(`\n${retailer} (${this.formatCurrency(retailerBudget)})\n`);

      retailerCampaigns.forEach((campaign) => {
        sections.push(this.formatTextCampaign(campaign));
      });
    }

    return sections.join("\n");
  }

  formatTextFutureCampaigns(campaigns) {
    if (campaigns.length === 0) {
      return "\nNo upcoming campaigns.\n";
    }

    const sections = [];

    // Group by month
    const byMonth = campaigns.reduce((acc, campaign) => {
      const month = format(
        parseISO(campaign["Tactic Start Date"]),
        "MMMM yyyy"
      );
      if (!acc[month]) acc[month] = [];
      acc[month].push(campaign);
      return acc;
    }, {});

    for (const [month, monthCampaigns] of Object.entries(byMonth)) {
      const monthBudget = monthCampaigns.reduce(
        (sum, c) => sum + parseFloat(c["Tactic Allocated Budget"]),
        0
      );

      sections.push(`\n${month} (${this.formatCurrency(monthBudget)})\n`);

      // Sub-group by retailer
      const byRetailer = monthCampaigns.reduce((acc, campaign) => {
        const retailer = campaign.Retailer;
        if (!acc[retailer]) acc[retailer] = [];
        acc[retailer].push(campaign);
        return acc;
      }, {});

      for (const [retailer, retailerCampaigns] of Object.entries(byRetailer)) {
        const retailerBudget = retailerCampaigns.reduce(
          (sum, c) => sum + parseFloat(c["Tactic Allocated Budget"]),
          0
        );

        sections.push(
          `  ${retailer} (${this.formatCurrency(retailerBudget)})\n`
        );

        retailerCampaigns.forEach((campaign) => {
          sections.push(this.formatTextCampaign(campaign, 2));
        });
      }
    }

    return sections.join("\n");
  }

  formatTextCampaign(campaign, baseIndent = 0) {
    const indent = " ".repeat(baseIndent);
    const sections = [];
    const isNew = campaign.changes?.includes("New Campaign");
    const hasChanges = campaign.changes?.length > 0 && !isNew;

    // Campaign header
    sections.push(
      `${indent}${campaign["Tactic Brand"]} ${isNew ? "[NEW] " : ""}${
        hasChanges ? "[UPDATED] " : ""
      }`
    );

    // Campaign details
    sections.push(
      `${indent}Event: ${campaign["Event Name"]}`,
      `${indent}Event ID: ${campaign["Event ID"]} (https://cemm-ajinomoto.shopperationsapp.com/events/${campaign["Event ID"]}/spend)`,
      `${indent}Product: ${campaign["Tactic Product"]}`,
      `${indent}Campaign: ${campaign["Tactic Name"]}`,
      campaign["Tactic Description"]
        ? `${indent}Description: ${campaign["Tactic Description"]}`
        : null,
      campaign["Tactic Vendor"]
        ? `${indent}Vendor: ${campaign["Tactic Vendor"]}`
        : null,
      `${indent}Dates: ${format(
        parseISO(campaign["Tactic Start Date"]),
        this.dateFormat
      )} to ${format(parseISO(campaign["Tactic End Date"]), this.dateFormat)}`,
      `${indent}Budget: ${this.formatCurrency(
        parseFloat(campaign["Tactic Allocated Budget"])
      )}`,
      `${indent}Order ID: ${campaign["Tactic Order ID"]}`
    );

    // Changes section
    if (hasChanges) {
      sections.push(
        `${indent}Changes:`,
        ...campaign.changes.map((change) => `${indent}- ${change}`)
      );
    }

    sections.push(""); // Add blank line after each campaign

    return sections.filter(Boolean).join("\n");
  }
}

module.exports = CampaignProcessor;

```

## File: middleware.ts
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrcmiddlewarets'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/middleware.ts

```typescript
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  // Handle CORS
  const response = NextResponse.next();

  response.headers.set("Access-Control-Allow-Origin", "*");
  response.headers.set(
    "Access-Control-Allow-Methods",
    "GET, POST, PUT, DELETE, OPTIONS"
  );
  response.headers.set(
    "Access-Control-Allow-Headers",
    "Content-Type, Authorization"
  );

  // Handle uploads
  if (request.nextUrl.pathname.startsWith("/api/process")) {
    const contentType = request.headers.get("content-type");
    if (!contentType?.includes("multipart/form-data")) {
      return new NextResponse("Invalid content type", { status: 400 });
    }
  }

  return response;
}

export const config = {
  matcher: "/api/:path*",
};

```

## File: api.ts
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrctypesapits'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/types/api.ts

```typescript
export interface ApiResponse<T = any> {
    success: boolean;
    message?: string;
    data?: T;
  }
  
  export interface ProcessResponse extends ApiResponse {
    data?: {
      filename: string;
      result: string;
    };
  }
  
  export interface ReportResponse extends ApiResponse {
    content?: string;
  }
  
  export interface ProcessRequestBody {
    file: File;
    primaryEmails: string[];
    ccEmails: string[];
  }
```

## File: layout.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrcapplayouttsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/app/layout.tsx

```tsx
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Campaign Report Processor',
  description: 'Process and distribute campaign reports',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
```

## File: page.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrcapppagetsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/app/page.tsx

```tsx
'use client'

import { CampaignReportProcessor } from "@/components/campaign-report-processor"

export default function Home() {
  return (
    <main className="min-h-screen p-4 bg-background">
      <CampaignReportProcessor />
    </main>
  )
}
```

## File: globals.css
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrcappglobalscss'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/app/globals.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  font-family: Arial, Helvetica, sans-serif;
}

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 0 0% 3.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 0 0% 3.9%;
    --primary: 0 0% 9%;
    --primary-foreground: 0 0% 98%;
    --secondary: 0 0% 96.1%;
    --secondary-foreground: 0 0% 9%;
    --muted: 0 0% 96.1%;
    --muted-foreground: 0 0% 45.1%;
    --accent: 0 0% 96.1%;
    --accent-foreground: 0 0% 9%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 0 0% 98%;
    --border: 0 0% 89.8%;
    --input: 0 0% 89.8%;
    --ring: 0 0% 3.9%;
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
    --chart-3: 197 37% 24%;
    --chart-4: 43 74% 66%;
    --chart-5: 27 87% 67%;
    --radius: 0.5rem;
  }
  .dark {
    --background: 0 0% 3.9%;
    --foreground: 0 0% 98%;
    --card: 0 0% 3.9%;
    --card-foreground: 0 0% 98%;
    --popover: 0 0% 3.9%;
    --popover-foreground: 0 0% 98%;
    --primary: 0 0% 98%;
    --primary-foreground: 0 0% 9%;
    --secondary: 0 0% 14.9%;
    --secondary-foreground: 0 0% 98%;
    --muted: 0 0% 14.9%;
    --muted-foreground: 0 0% 63.9%;
    --accent: 0 0% 14.9%;
    --accent-foreground: 0 0% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 0 0% 98%;
    --border: 0 0% 14.9%;
    --input: 0 0% 14.9%;
    --ring: 0 0% 83.1%;
    --chart-1: 220 70% 50%;
    --chart-2: 160 60% 45%;
    --chart-3: 30 80% 55%;
    --chart-4: 280 65% 60%;
    --chart-5: 340 75% 55%;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
  }
}

```

## File: route.ts
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrcappapireporttypefilenameroutets'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/app/api/report/[type]/[filename]/route.ts

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { readFile } from 'fs/promises';
import path from 'path';

interface RouteParams {
  params: {
    type: string;
    filename: string;
  };
}

export async function GET(
  request: NextRequest,
  context: RouteParams
): Promise<NextResponse> {
  try {
    // Await the params to ensure they're accessed asynchronously
    const params = await Promise.resolve(context.params);
    const { type, filename } = params;

    // Validate type parameter
    if (!['md', 'txt'].includes(type)) {
      return NextResponse.json(
        { success: false, message: 'Invalid report type' },
        { status: 400 }
      );
    }

    // Validate filename to prevent directory traversal
    if (filename.includes('..') || !filename.match(/^[a-zA-Z0-9_\-\.]+$/)) {
      return NextResponse.json(
        { success: false, message: 'Invalid filename' },
        { status: 400 }
      );
    }

    const outputDir = path.join(process.cwd(), 'data', 'output');
    const filePath = path.join(outputDir, filename);

    try {
      const content = await readFile(filePath, 'utf-8');
      
      // Set appropriate content type and disposition headers
      const contentType = type === 'md' ? 'text/markdown' : 'text/plain';
      
      return new NextResponse(content, {
        headers: {
          'Content-Type': contentType,
          'Content-Disposition': `inline; filename="${filename}"`,
          'Cache-Control': 'no-cache, no-store, must-revalidate',
          'Pragma': 'no-cache',
          'Expires': '0'
        }
      });
    } catch (error) {
      console.error('File read error:', error);
      return NextResponse.json(
        { success: false, message: 'Report not found' },
        { status: 404 }
      );
    }
  } catch (error) {
    console.error('Error fetching report:', error);
    return NextResponse.json(
      { 
        success: false, 
        message: error instanceof Error ? error.message : 'Failed to fetch report' 
      },
      { status: 500 }
    );
  }
}
```

## File: route.ts
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrcappapiprocessroutets'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/app/api/process/route.ts

```typescript
import { NextResponse } from 'next/server';
import { writeFile } from 'fs/promises';
import path from 'path';
import { spawn } from 'child_process';
import yaml from 'yaml';

// Helper function to run Python script
async function runPythonScript(configPath: string): Promise<any> {
  return new Promise((resolve, reject) => {
    const scriptPath = path.join(process.cwd(), 'python', 'process_campaign.py');
    const pythonProcess = spawn('python', [scriptPath, '--config', configPath]);
    
    let stdout = '';
    let stderr = '';

    pythonProcess.stdout.on('data', (data) => {
      stdout += data.toString();
      console.log(`Python stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
      stderr += data.toString();
      console.log(`Python stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
      console.log('Python process completed with code:', code);
      console.log('stdout:', stdout);
      console.log('stderr:', stderr);
      
      if (code !== 0) {
        reject(new Error(`Python script failed (code ${code}): ${stderr}`));
      } else {
        try {
          // Try to parse stdout as JSON
          const result = JSON.parse(stdout);
          resolve(result);
        } catch (e) {
          console.error('Failed to parse Python output as JSON:', e);
          resolve({ stdout, stderr });
        }
      }
    });
  });
}

export async function POST(request: Request) {
  try {
    const formData = await request.formData();
    const file: File | null = formData.get('file') as unknown as File;
    const primaryEmails = JSON.parse(formData.get('primaryEmails') as string);
    const ccEmails = JSON.parse(formData.get('ccEmails') as string);

    if (!file) {
      return NextResponse.json(
        { success: false, message: 'No file uploaded' },
        { status: 400 }
      );
    }

    // Create necessary directories
    const uploadsDir = path.join(process.cwd(), 'data', 'uploads');
    const configDir = path.join(process.cwd(), 'data', 'config');
    const outputDir = path.join(process.cwd(), 'data', 'output');

    // Generate unique filename
    const timestamp = new Date().toISOString().replace(/[^0-9]/g, '');
    const filename = `campaign_report_${timestamp}.csv`;
    const filepath = path.join(uploadsDir, filename);

    // Write the uploaded file
    const bytes = await file.arrayBuffer();
    const buffer = Buffer.from(bytes);
    await writeFile(filepath, buffer);

    // Create config file for this run
    const configData = {
      input_offsite_csv: filepath,
      output_dir: outputDir,
      email_config: {
        sender_email: process.env.EMAIL_SENDER,
        sender_password: process.env.EMAIL_SENDER_PASSWORD,
        smtp_server: process.env.EMAIL_SMTP_SERVER || "smtp.office365.com",
        smtp_port: parseInt(process.env.EMAIL_SMTP_PORT || "587"),
        primary_recipients: primaryEmails,
        cc_recipients: ccEmails
      }
    };

    const configPath = path.join(configDir, `config_${timestamp}.yaml`);
    await writeFile(configPath, yaml.stringify(configData));

    console.log('Running Python script with config:', configPath);
    const result = await runPythonScript(configPath);
    console.log('Python script result:', result);

    if (!result.success) {
      throw new Error(result.error || 'Python script failed');
    }

    return NextResponse.json({
      success: true,
      data: result
    });

  } catch (error) {
    console.error('Error processing report:', error);
    return NextResponse.json(
      { 
        success: false, 
        message: error instanceof Error ? error.message : 'Failed to process report'
      },
      { status: 500 }
    );
  }
}
```

## File: campaign-report-processor.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentscampaignreportprocessortsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/campaign-report-processor.tsx

```tsx
// /src/app/components/campaign-report-processor.tsx

"use client";

import React, { useState, useEffect } from "react";
import {
  Upload,
  FileText,
  Mail,
  AlertCircle,
  CheckCircle2,
  Plus,
  X,
} from "lucide-react";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import { Separator } from "@/components/ui/separator";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import ReactMarkdown from "react-markdown";

type ProcessingStatus = "idle" | "ready" | "processing" | "success" | "error";

interface ProcessResult {
  success: boolean;
  message?: string;
  data?: {
    markdown_path?: string;
    email_path?: string;
    campaign_count?: number;
    changes_detected?: number;
  };
}

export function CampaignReportProcessor() {
  const [file, setFile] = useState<File | null>(null);
  const [processing, setProcessing] = useState(false);
  const [progress, setProgress] = useState(0);
  const [status, setStatus] = useState<ProcessingStatus>("idle");
  const [markdownContent, setMarkdownContent] = useState("");
  const [error, setError] = useState("");

  const [newPrimaryEmail, setNewPrimaryEmail] = useState("");
  const [newCCEmail, setNewCCEmail] = useState("");
  const [primaryEmails, setPrimaryEmails] = useState<string[]>([]);
  const [ccEmails, setCCEmails] = useState<string[]>([]);
  const [emailError, setEmailError] = useState("");

  useEffect(() => {
    const storedPrimary = localStorage.getItem("primaryEmails");
    const storedCC = localStorage.getItem("ccEmails");

    if (storedPrimary) setPrimaryEmails(JSON.parse(storedPrimary));
    if (storedCC) setCCEmails(JSON.parse(storedCC));
  }, []);

  useEffect(() => {
    localStorage.setItem("primaryEmails", JSON.stringify(primaryEmails));
    localStorage.setItem("ccEmails", JSON.stringify(ccEmails));
  }, [primaryEmails, ccEmails]);

  const validateEmail = (email: string): boolean => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  };

  const addEmail = (type: "primary" | "cc", email: string) => {
    setEmailError("");

    if (!email) {
      setEmailError("Please enter an email address");
      return;
    }

    if (!validateEmail(email)) {
      setEmailError("Please enter a valid email address");
      return;
    }

    if (type === "primary") {
      if (primaryEmails.includes(email) || ccEmails.includes(email)) {
        setEmailError("Email already exists in the lists");
        return;
      }
      setPrimaryEmails([...primaryEmails, email]);
      setNewPrimaryEmail("");
    } else {
      if (ccEmails.includes(email) || primaryEmails.includes(email)) {
        setEmailError("Email already exists in the lists");
        return;
      }
      setCCEmails([...ccEmails, email]);
      setNewCCEmail("");
    }
  };

  const removeEmail = (type: "primary" | "cc", email: string) => {
    if (type === "primary") {
      setPrimaryEmails(primaryEmails.filter((e) => e !== email));
    } else {
      setCCEmails(ccEmails.filter((e) => e !== email));
    }
  };

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = event.target.files?.[0];
    if (selectedFile && selectedFile.name.endsWith(".csv")) {
      setFile(selectedFile);
      setError("");
      setStatus("ready");
    } else {
      setError("Please select a valid CSV file");
      setFile(null);
      setStatus("idle");
    }
  };

  const processReport = async () => {
    if (!file || primaryEmails.length === 0) {
      setError("Please select a file and add at least one primary email recipient");
      return;
    }
  
    setProcessing(true);
    setProgress(0);
    setStatus("processing");
    setMarkdownContent("");
  
    try {
      // Show upload progress
      setProgress(20);
  
      // Validate file size for Vercel limits (max 50MB)
      if (file.size > 50 * 1024 * 1024) {
        throw new Error("File size exceeds 50MB limit");
      }
  
      const formData = new FormData();
      formData.append("file", file);
      formData.append("primaryEmails", JSON.stringify(primaryEmails));
      formData.append("ccEmails", JSON.stringify(ccEmails));
  
      // Add request timeout for Vercel's 10s limit
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 9500); // 9.5s timeout
  
      setProgress(40);
  
      const response = await fetch("/api/process", {
        method: "POST",
        body: formData,
        signal: controller.signal,
      }).finally(() => clearTimeout(timeout));
  
      setProgress(60);
  
      const result = await response.json() as ProcessResult;
      
      if (!result.success) {
        throw new Error(result.message || "Failed to process report");
      }
  
      setProgress(80);
  
      // Fetch the markdown content
      if (result.data?.markdown_path) {
        const filename = result.data.markdown_path.split("/").pop();
        if (!filename) {
          throw new Error("Invalid markdown filename");
        }
  
        // Add timeout for markdown fetch
        const mdController = new AbortController();
        const mdTimeout = setTimeout(() => mdController.abort(), 9500);
  
        try {
          const markdownResponse = await fetch(`/api/report/md/${filename}`, {
            signal: mdController.signal,
            headers: {
              'Cache-Control': 'no-cache',
              'Pragma': 'no-cache'
            }
          }).finally(() => clearTimeout(mdTimeout));
  
          if (!markdownResponse.ok) {
            const errorText = await markdownResponse.text();
            console.error('Markdown fetch error:', errorText);
            throw new Error(`Failed to fetch report: ${markdownResponse.statusText}`);
          }
  
          const content = await markdownResponse.text();
          
          // Validate content
          if (!content || content.trim().length === 0) {
            throw new Error("Received empty report content");
          }
  
          setMarkdownContent(content);
  
          // Log successful processing metrics
          if (result.data?.campaign_count) {
            console.log(`Processed ${result.data.campaign_count} campaigns`);
          }
          if (result.data?.changes_detected) {
            console.log(`Detected ${result.data.changes_detected} changes`);
          }
        } catch (err) {
          if (err instanceof Error && err.name === 'AbortError') {
            throw new Error("Report fetch timed out - please try again");
          }
          throw err;
        }
      } else {
        throw new Error("No report was generated");
      }
  
      setStatus("success");
      setProgress(100);
  
    } catch (err) {
      console.error("Error processing report:", err);
      
      // Handle specific error types
      let errorMessage = "An error occurred";
      if (err instanceof Error) {
        if (err.name === 'AbortError') {
          errorMessage = "Request timed out - please try again";
        } else if (err.message.includes("Failed to fetch")) {
          errorMessage = "Network error - please check your connection";
        } else {
          errorMessage = err.message;
        }
      }
      
      setError(errorMessage);
      setStatus("error");
      setProgress(0);
    } finally {
      setProcessing(false);
    }
  };

  const renderStatus = () => {
    switch (status) {
      case "ready":
        return (
          <Alert className="mb-4">
            <FileText className="h-4 w-4" />
            <AlertDescription>File selected: {file?.name}</AlertDescription>
          </Alert>
        );
      case "processing":
        return (
          <div className="space-y-4 mb-4">
            <Alert>
              <AlertDescription>Processing campaign report...</AlertDescription>
            </Alert>
            <Progress value={progress} className="w-full" />
          </div>
        );
      case "success":
        return (
          <Alert className="mb-4">
            <CheckCircle2 className="h-4 w-4 text-green-500" />
            <AlertDescription>
              Report processed and distributed successfully!
            </AlertDescription>
          </Alert>
        );
      case "error":
        return (
          <Alert variant="destructive" className="mb-4">
            <AlertCircle className="h-4 w-4" />
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        );
      default:
        return null;
    }
  };

  return (
    <Card className="mt-4">
      <CardHeader>
        <CardTitle>Campaign Report Processor</CardTitle>
        <CardDescription>
          Upload a CSV report file to process and distribute campaign
          information
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-6">
          {/* Email Recipients Section */}
          <div className="space-y-4">
            <h3 className="text-lg font-medium">Email Recipients</h3>

            {emailError && (
              <Alert variant="destructive" className="mb-4">
                <AlertCircle className="h-4 w-4" />
                <AlertDescription>{emailError}</AlertDescription>
              </Alert>
            )}

            {/* Primary Recipients */}
            <div className="space-y-2">
              <Label>Primary Recipients</Label>
              <div className="flex gap-2">
                <Input
                  type="email"
                  placeholder="Enter email address"
                  value={newPrimaryEmail}
                  onChange={(e) => setNewPrimaryEmail(e.target.value)}
                  onKeyPress={(e) => {
                    if (e.key === "Enter") {
                      addEmail("primary", newPrimaryEmail);
                    }
                  }}
                />
                <Button
                  onClick={() => addEmail("primary", newPrimaryEmail)}
                  size="icon"
                >
                  <Plus className="h-4 w-4" />
                </Button>
              </div>
              <div className="flex flex-wrap gap-2 mt-2">
                {primaryEmails.map((email) => (
                  <Badge
                    key={email}
                    variant="secondary"
                    className="flex items-center gap-1"
                  >
                    {email}
                    <button
                      onClick={() => removeEmail("primary", email)}
                      className="ml-1 hover:text-destructive"
                    >
                      <X className="h-3 w-3" />
                    </button>
                  </Badge>
                ))}
              </div>
            </div>

            {/* CC Recipients */}
            <div className="space-y-2">
              <Label>CC Recipients</Label>
              <div className="flex gap-2">
                <Input
                  type="email"
                  placeholder="Enter email address"
                  value={newCCEmail}
                  onChange={(e) => setNewCCEmail(e.target.value)}
                  onKeyPress={(e) => {
                    if (e.key === "Enter") {
                      addEmail("cc", newCCEmail);
                    }
                  }}
                />
                <Button onClick={() => addEmail("cc", newCCEmail)} size="icon">
                  <Plus className="h-4 w-4" />
                </Button>
              </div>
              <div className="flex flex-wrap gap-2 mt-2">
                {ccEmails.map((email) => (
                  <Badge
                    key={email}
                    variant="secondary"
                    className="flex items-center gap-1"
                  >
                    {email}
                    <button
                      onClick={() => removeEmail("cc", email)}
                      className="ml-1 hover:text-destructive"
                    >
                      <X className="h-3 w-3" />
                    </button>
                  </Badge>
                ))}
              </div>
            </div>
          </div>

          <Separator />

          {/* File Upload Section */}
          <div className="flex flex-col items-center justify-center border-2 border-dashed rounded-lg p-6 bg-muted/50">
            <input
              type="file"
              accept=".csv"
              onChange={handleFileChange}
              className="hidden"
              id="file-upload"
            />
            <label
              htmlFor="file-upload"
              className="flex flex-col items-center cursor-pointer"
            >
              <Upload className="h-8 w-8 mb-2 text-muted-foreground" />
              <span className="text-sm text-muted-foreground">
                Click to upload or drag and drop
              </span>
              <span className="text-xs text-muted-foreground mt-1">
                CSV files only
              </span>
            </label>
          </div>

          {/* Status Display */}
          {renderStatus()}

          {/* Process Button */}
          <div className="flex justify-center">
            <Button
              onClick={processReport}
              disabled={!file || processing || primaryEmails.length === 0}
              className="w-full md:w-auto"
            >
              {processing ? (
                <span className="flex items-center">Processing...</span>
              ) : (
                <span className="flex items-center">
                  <Mail className="mr-2 h-4 w-4" />
                  Process and Distribute Report
                </span>
              )}
            </Button>
          </div>

          {/* Report Output */}
          {markdownContent && (
            <Card className="mt-6">
              <CardHeader>
                <CardTitle>Generated Report</CardTitle>
              </CardHeader>
              <CardContent>
                <Tabs defaultValue="rendered" className="w-full">
                  <TabsList>
                    <TabsTrigger value="rendered">Rendered</TabsTrigger>
                    <TabsTrigger value="source">Source</TabsTrigger>
                  </TabsList>
                  <TabsContent value="rendered" className="mt-4">
                    <ScrollArea className="h-[600px] w-full rounded-md border p-4">
                      <div className="prose prose-sm dark:prose-invert max-w-none">
                        <ReactMarkdown>{markdownContent}</ReactMarkdown>
                      </div>
                    </ScrollArea>
                  </TabsContent>
                  <TabsContent value="source" className="mt-4">
                    <ScrollArea className="h-[600px] w-full rounded-md border p-4">
                      <pre className="whitespace-pre-wrap font-mono text-sm">
                        {markdownContent}
                      </pre>
                    </ScrollArea>
                  </TabsContent>
                </Tabs>
              </CardContent>
            </Card>
          )}
        </div>
      </CardContent>
    </Card>
  );
}

```

## File: tabs.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuitabstsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/tabs.tsx

```tsx
"use client"

import * as React from "react"
import * as TabsPrimitive from "@radix-ui/react-tabs"

import { cn } from "@/lib/utils"

const Tabs = TabsPrimitive.Root

const TabsList = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.List>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.List
    ref={ref}
    className={cn(
      "inline-flex h-9 items-center justify-center rounded-lg bg-muted p-1 text-muted-foreground",
      className
    )}
    {...props}
  />
))
TabsList.displayName = TabsPrimitive.List.displayName

const TabsTrigger = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Trigger
    ref={ref}
    className={cn(
      "inline-flex items-center justify-center whitespace-nowrap rounded-md px-3 py-1 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow",
      className
    )}
    {...props}
  />
))
TabsTrigger.displayName = TabsPrimitive.Trigger.displayName

const TabsContent = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Content>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Content
    ref={ref}
    className={cn(
      "mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
      className
    )}
    {...props}
  />
))
TabsContent.displayName = TabsPrimitive.Content.displayName

export { Tabs, TabsList, TabsTrigger, TabsContent }

```

## File: card.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuicardtsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/card.tsx

```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-xl border bg-card text-card-foreground shadow",
      className
    )}
    {...props}
  />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("font-semibold leading-none tracking-tight", className)}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex items-center p-6 pt-0", className)}
    {...props}
  />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }

```

## File: progress.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuiprogresstsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/progress.tsx

```tsx
"use client"

import * as React from "react"
import * as ProgressPrimitive from "@radix-ui/react-progress"

import { cn } from "@/lib/utils"

const Progress = React.forwardRef<
  React.ElementRef<typeof ProgressPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ProgressPrimitive.Root>
>(({ className, value, ...props }, ref) => (
  <ProgressPrimitive.Root
    ref={ref}
    className={cn(
      "relative h-2 w-full overflow-hidden rounded-full bg-primary/20",
      className
    )}
    {...props}
  >
    <ProgressPrimitive.Indicator
      className="h-full w-full flex-1 bg-primary transition-all"
      style={{ transform: `translateX(-${100 - (value || 0)}%)` }}
    />
  </ProgressPrimitive.Root>
))
Progress.displayName = ProgressPrimitive.Root.displayName

export { Progress }

```

## File: scroll-area.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuiscrollareatsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/scroll-area.tsx

```tsx
"use client"

import * as React from "react"
import * as ScrollAreaPrimitive from "@radix-ui/react-scroll-area"

import { cn } from "@/lib/utils"

const ScrollArea = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.Root>
>(({ className, children, ...props }, ref) => (
  <ScrollAreaPrimitive.Root
    ref={ref}
    className={cn("relative overflow-hidden", className)}
    {...props}
  >
    <ScrollAreaPrimitive.Viewport className="h-full w-full rounded-[inherit]">
      {children}
    </ScrollAreaPrimitive.Viewport>
    <ScrollBar />
    <ScrollAreaPrimitive.Corner />
  </ScrollAreaPrimitive.Root>
))
ScrollArea.displayName = ScrollAreaPrimitive.Root.displayName

const ScrollBar = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>
>(({ className, orientation = "vertical", ...props }, ref) => (
  <ScrollAreaPrimitive.ScrollAreaScrollbar
    ref={ref}
    orientation={orientation}
    className={cn(
      "flex touch-none select-none transition-colors",
      orientation === "vertical" &&
        "h-full w-2.5 border-l border-l-transparent p-[1px]",
      orientation === "horizontal" &&
        "h-2.5 flex-col border-t border-t-transparent p-[1px]",
      className
    )}
    {...props}
  >
    <ScrollAreaPrimitive.ScrollAreaThumb className="relative flex-1 rounded-full bg-border" />
  </ScrollAreaPrimitive.ScrollAreaScrollbar>
))
ScrollBar.displayName = ScrollAreaPrimitive.ScrollAreaScrollbar.displayName

export { ScrollArea, ScrollBar }

```

## File: label.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuilabeltsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/label.tsx

```tsx
"use client"

import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const labelVariants = cva(
  "text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
)

const Label = React.forwardRef<
  React.ElementRef<typeof LabelPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof LabelPrimitive.Root> &
    VariantProps<typeof labelVariants>
>(({ className, ...props }, ref) => (
  <LabelPrimitive.Root
    ref={ref}
    className={cn(labelVariants(), className)}
    {...props}
  />
))
Label.displayName = LabelPrimitive.Root.displayName

export { Label }

```

## File: alert.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuialerttsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/alert.tsx

```tsx
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const alertVariants = cva(
  "relative w-full rounded-lg border px-4 py-3 text-sm [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4 [&>svg]:text-foreground [&>svg~*]:pl-7",
  {
    variants: {
      variant: {
        default: "bg-background text-foreground",
        destructive:
          "border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

const Alert = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & VariantProps<typeof alertVariants>
>(({ className, variant, ...props }, ref) => (
  <div
    ref={ref}
    role="alert"
    className={cn(alertVariants({ variant }), className)}
    {...props}
  />
))
Alert.displayName = "Alert"

const AlertTitle = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
  <h5
    ref={ref}
    className={cn("mb-1 font-medium leading-none tracking-tight", className)}
    {...props}
  />
))
AlertTitle.displayName = "AlertTitle"

const AlertDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm [&_p]:leading-relaxed", className)}
    {...props}
  />
))
AlertDescription.displayName = "AlertDescription"

export { Alert, AlertTitle, AlertDescription }

```

## File: badge.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuibadgetsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/badge.tsx

```tsx
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default:
          "border-transparent bg-primary text-primary-foreground shadow hover:bg-primary/80",
        secondary:
          "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
        destructive:
          "border-transparent bg-destructive text-destructive-foreground shadow hover:bg-destructive/80",
        outline: "text-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  )
}

export { Badge, badgeVariants }

```

## File: separator.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuiseparatortsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/separator.tsx

```tsx
"use client"

import * as React from "react"
import * as SeparatorPrimitive from "@radix-ui/react-separator"

import { cn } from "@/lib/utils"

const Separator = React.forwardRef<
  React.ElementRef<typeof SeparatorPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof SeparatorPrimitive.Root>
>(
  (
    { className, orientation = "horizontal", decorative = true, ...props },
    ref
  ) => (
    <SeparatorPrimitive.Root
      ref={ref}
      decorative={decorative}
      orientation={orientation}
      className={cn(
        "shrink-0 bg-border",
        orientation === "horizontal" ? "h-[1px] w-full" : "h-full w-[1px]",
        className
      )}
      {...props}
    />
  )
)
Separator.displayName = SeparatorPrimitive.Root.displayName

export { Separator }

```

## File: button.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuibuttontsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/button.tsx

```tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default:
          "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline:
          "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }

```

## File: input.tsx
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrccomponentsuiinputtsx'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/components/ui/input.tsx

```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

const Input = React.forwardRef<HTMLInputElement, React.ComponentProps<"input">>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = "Input"

export { Input }

```

## File: utils.ts
### Path: <a id='Usersjaredkirbyllm_projectscampaignreportgeneratorsrclibutilsts'></a>/Users/jaredkirby/llm_projects/campaign-report-generator/src/lib/utils.ts

```typescript
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

```

