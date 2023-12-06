import { SystemTable, OptionTable, SSTable } from './tables.js'
import { NetworkForm, SecurityForm, ArchivingForm, DataCenterForm, ICTForm } from './forms.js'

class TableSection {
    constructor(sectionId, tables) {
        this.sectionId = sectionId;
        this.tables = tables;
    }
}

var hardware = new TableSection(
    'hardware',
    [
        new OptionTable(
            `Number of Computing Devices and Peripherals by Type and by Year Acquired`,
            [
                `Mainframe`,
                `Servers`,
                `Desktop PC`,
                `Laptop / Notebook / Netbook PC`,
                `Mobile Phone (incl. smart phones)`,
                `Tablet PC`,
                `Multi-function printer (print, copy, etc.)`,
                `Printer only`,
                `Digital Camera (Include DSLR, if any)`,
                `Wide-format Printer or Plotter`,
                `Small Scanner (ex. flatbed scanner)`,
                `Smart Card Reader`,
                `Wide-format Scanner`,
                `External Hard Drive`,
                `Generator Set`,
                `Others`
            ],
            8,
            `cd-year`,
            `<thead class="table-light">
                <tr>
                <th scope="col" rowspan="3" style="width: 300px">Types</th>
                <th scope="" colspan="7">Total number of functioning units by year acquired</th>
                </tr>
                <tr>
                <th scope="col" colspan="2">Last Year</th>
                <th scope="col" colspan="2">Last 2 Years</th>
                <th scope="col" colspan="2">Last 3 Years</th>
                <th scope="col" rowspan="2">More than 3 years</th>
                </tr>
                <tr>
                <th scope="col">Owned</th>
                <th scope="col">Leased</th>
                <th scope="col">Owned</th>
                <th scope="col">Leased</th>
                <th scope="col">Owned</th>
                <th scope="col">Leased</th>
                </tr>
            </thead>`,
            { '0': true }),
        new OptionTable(
            `Number of Computing Devices and Peripherals by Usage`,
            [
                `Servers`,
                `Desktop PC`,
                `Laptop / Notebook / Netbook PC`,
                `Multi-function printer (print, copy, etc.)`,
                `Printer only`
            ],
            6,
            `cd-usage`,
            `<thead class="table-light">
                <tr>
                <th scope="col" rowspan="2" style="width: 200px">Types</th>
                <th scope="col" colspan="3">Operations</th>
                <th scope="col" rowspan="2">General Administration and Support Services Support to Operations</th>
                <th scope="col" rowspan="2">Projects</th>
                </tr>
                <tr>
                <th scope="col">Employees</th>
                <th scope="col">Training</th>
                <th scope="col">Frontline Services</th>
                </tr>
            </thead>`,
            { '0': true }),
        new OptionTable(
            `Number of Servers by Capacity and by Location`,
            [
                `Above 4 TB`,
                `2 TB to 4 TB`,
                `Below 2 TB`,
            ],
            3,
            `servers`,
            `<thead class="table-light">
                <tr>
                <th scope="col" rowspan="2" style="width: 200px">Total Capacity of HDD</th>
                <th scope="col" colspan="2">Location</th>
                </tr>
                <tr>
                <th scope="col">In-house</th>
                <th scope="col">Co-located</th>
                </tr>
            </thead>`,
            { '0': true })
    ]
);

var software = new TableSection(
    'software',
    [
        new OptionTable(
            `OS for stand-alone PCs (desktops and laptops)`,
            [
                `Older than Windows XP`,
                `Windows XP`,
                `Windows Vista`,
                `Windows 7`,
                `Windows 8 and up`,
                `Linux`,
                `Mac OS`,
                `Mac OS X`,
                `Others`,
            ],
            3,
            `pc-os`,
            `<thead class="table-light">
                <tr>
                <th scope="col" style="width: 200px">Operating System</th>
                <th scope="col">Lifetime License</th>
                <th scope="col">If not, write below the year of expiration</th>
                </tr>
            </thead>`,
            { '0': true },
            { '1': true }
        ),
        new OptionTable(
            `OS for workstations (desktops and laptops)`,
            [
                `Older than Windows XP`,
                `Windows NT`,
                `Windows XP`,
                `Windows Vista`,
                `Windows 7`,
                `Windows 8 and up`,
                `Solaris`,
                `Linux`,
                `Mac OS`,
                `Others`,
            ],
            3,
            `ws-os`,
            `<thead class="table-light">
                <tr>
                <th scope="col" style="width: 200px">Operating System</th>
                <th scope="col">Lifetime License</th>
                <th scope="col">If not, write below the year of expiration</th>
                </tr>
            </thead>`,
            { '0': true },
            { '1': true }
        ),
        new OptionTable(
            `OS for servers`,
            [
                `Windows NT`,
                `Windows 2000`,
                `Windows Server 2003`,
                `Windows Server 2008`,
                `Windows Server 2012`,
                `Solaris`,
                `OpenSolaris`,
                `OS/2`,
                `Linux`,
                `Mac OS X Server`,
                `Others`,
            ],
            3,
            `server-os`,
            `<thead class="table-light">
                <tr>
                <th scope="col" style="width: 200px">Operating System</th>
                <th scope="col">Lifetime License</th>
                <th scope="col">If not, write below the year of expiration</th>
                </tr>
            </thead>`,
            [true, false, false],
            [false, true, false]
        ),
        new OptionTable(
            `Office automation software`,
            [
                `Older than MS Office 2003`,
                `MS Office 2003`,
                `MS Office XP`,
                `MS Office 2007`,
                `MS Office 2010`,
                `MS Visio`,
                `MS Project`,
                `Open Project`,
                `Open Office`,
                `Others`
            ],
            3,
            `automation-software`,
            `<thead class="table-light">
                <tr>
                <th scope="col" style="width: 200px">Software / Application Package </th>
                <th scope="col">Lifetime License</th>
                <th scope="col">If not, write below the year of expiration</th>
                </tr>
            </thead>`,
            { '0': true },
            { '1': true }
        ),
        new SystemTable(
            `Operational Oversight / Administrative Systems`,
            6,
            `admin-systems`,
            `<thead class="table-light">
                <tr>
                <th scope="col">Name of System </th>
                <th scope="col">Own Intellectual Property</th>
                <th scope="col">Development Platform</th>
                <th scope="col">Working Environment</th>
                <th scope="col">Maintenance Cost</th>
                <th scope="col">Use</th>
                </tr>
            </thead>`,
            [true, false, true, true, true, true],
            [false, true, false, false, false, false],
            { '3': ['S', 'C', 'W'] }
        ),
        new SystemTable(
            `Operational Strategic Information Systems`,
            6,
            `si-systems`,
            `<thead class="table-light">
                <tr>
                <th scope="col">Name of System </th>
                <th scope="col">Own Intellectual Property</th>
                <th scope="col">Development Platform</th>
                <th scope="col">Working Environment</th>
                <th scope="col">Maintenance Cost</th>
                <th scope="col">Use</th>
                </tr>
            </thead>`,
            { '0': true, '2': true, '3': true, '4': true, '5': true, },
            { '1': true },
            { '3': ['S', 'C', 'W'] }
        ),
        new SystemTable(
            `Databases`,
            6,
            `databases`,
            `<thead class="table-light">
                <tr>
                <th scope="col">Name of Database </th>
                <th scope="col">Own Intellectual Property</th>
                <th scope="col">Brief Description and Key Fields</th>
                <th scope="col">Database Management Software Used</th>
                <th scope="col">Maintenance Cost</th>
                <th scope="col">Use</th>
                </tr>
            </thead>`,
            { '0': true, '2': true, '3': true, '4': true, '5': true, },
            { '1': true },
        )
    ]
);

var network = new TableSection(
    `networkSection`,
    [new NetworkForm(
        ``,
        14,
        `network`,
        {},
    )]
);

var security = new TableSection(
    `securitySection`,
    [new SecurityForm(
        ``,
        2,
        `security`,
        {},
    )]
);

var archiving = new TableSection(
    `archivingSection`,
    [new ArchivingForm(
        ``,
        5,
        `archiving`,
        {},
    )]
);

var specialSolutions = new TableSection(
    `specialSolutions`,
    [new SSTable(
        ``,
        3,
        `special-solutions`,
        `<thead class="table-light">
            <tr>
            <th scope="col">Special Solutions Package </th>
            <th scope="col">Use</th>
            <th scope="col">Maintenance Cost</th>
            </tr>
        </thead>`,
        [true, true, true],
        {},
        {
            '0': 
            [  
                'Geographic Information System',
                'Automated Fingerprint Identification System',
                'Cloud computing',
                'CCTV System',
                'Others'
            ],
        },
        {
            '0' : 'Others',
            '1' : '15'
        }
    )]
);

var dataCenter = new TableSection(
    `datacenter`,
    [new DataCenterForm(
        ``,
        4,
        `data-center`,
        {},
    )]
);



var ict = new TableSection(
    `ict`,
    [new SystemTable(
        `Details of Ongoing ICT Projects`,
        8,
        `ict-projects`,
        `<thead class="table-light">
            <tr>
            <th scope="col" rowspan="2">Project name</th>
            <th scope="col" rowspan="2">Description</th>
            <th scope="col" colspan="2">Period</th>
            <th scope="col" rowspan="2">Cost (in pesos)</th>
            <th scope="col" rowspan="2">Development Strategy</th>
            <th scope="col" rowspan="2">Status</th>
            <th scope="col" rowspan="2">Use</th>
            </tr>
            <tr>
            <th scope="col">Start date</th>
            <th scope="col">End date</th>
            </tr>
        </thead>`,
        [true, true, true, true, true, true, true, true]

    ),
    new ICTForm(
        "Issues Encountered in the Implementation of ICT Projects",
        1,
        `ict-issues`,
        {},
    )]
);

export const ANNEXA5 = [
    hardware,
    software,
    network,
    security,
    archiving,
    dataCenter,
    specialSolutions,
    ict
];